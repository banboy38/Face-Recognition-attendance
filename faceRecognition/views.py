import os.path
import uuid
import base64

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
import face_recognition

from .models import StudentAttendance, StudentProfile, StudentAttendanceHistory, Courses


# Create your views here.


def _compare_faces(known_face, face_to_check, tolerance=0.7):
    try:
        known_face_encodings = face_recognition.load_image_file(known_face)
        unknown_face_encodings = face_recognition.load_image_file(face_to_check)

        known_face_encodings = face_recognition.face_encodings(known_face_encodings)[0]
        unknown_face_encodings = face_recognition.face_encodings(unknown_face_encodings)[0]

        results = face_recognition.compare_faces([known_face_encodings], unknown_face_encodings, tolerance)
        return results[0]
    except:
        return False


def studentProfile(request):
    if request.method == 'GET':
        if StudentProfile.objects.filter(user_id=request.user.id).exists():
            student_profile = StudentProfile.objects.get(user_id=request.user.id)
            print(student_profile.phone_no)
            return render(request, 'attendance/studentProfile.html', {'student_profile': student_profile})
        else:
            messages.warning(request, 'Your Profile is not created yet. Please contact your Teachers.')
            return render(request, 'attendance/studentProfile.html')
    else:
        messages.error(request, 'Invalid Request')
        return render(request, 'attendance/studentProfile.html')


def showAttendance(request):
    if request.method == 'GET':
        if StudentProfile.objects.filter(user_id=request.user.id).exists():
            attendance = StudentAttendance.objects.filter(user_id=request.user.id).select_related('course')
            course = Courses.objects.all()
            return render(request, 'attendance/showAttendance.html', {'attendance': attendance, 'courses': course})
        else:
            messages.warning(request, 'Your Profile is not created yet. Please contact your Teachers.')
            return render(request, 'attendance/showAttendance.html')
    elif request.method == 'POST':
        if StudentProfile.objects.filter(user_id=request.user.id).exists():
            course_id = request.POST.get('course')
            attendance = StudentAttendance.objects.filter(user_id=request.user.id, course_id=course_id)
            course = Courses.objects.all()
            return render(request, 'attendance/showAttendance.html', {'attendance': attendance, 'courses': course})
        else:
            messages.warning(request, 'Your Profile is not created yet. Please contact your Teachers.')
            return render(request, 'attendance/showAttendance.html')
    else:
        messages.error(request, 'Invalid Request')
        return render(request, 'attendance/showAttendance.html')


def studentAttendance(request):
    courses = Courses.objects.all()
    if request.method == 'GET':
        # Details of current user is passed to the webpage to be used in post method
        student_profile = StudentProfile.objects.get(user_id=request.user.id)
        return render(request, 'attendance/studentAttendance.html',
                      {'student_profile': student_profile, 'courses': courses})
    else:
        # Get the base64 image from the request
        image_base64 = request.POST.get('image_data')
        # convert this base64 to file and give it to model
        filename = str('photo_taken/' + str(uuid.uuid4()) + '.jpg')
        image_location = os.path.join(settings.MEDIA_ROOT, filename)
        image_file = open(image_location, 'wb')
        image_file.write(base64.b64decode(image_base64))
        image_file.close()

        # details of the student is passed to the function
        course = request.POST['course']
        course_details = Courses.objects.get(id=int(course))
        # Saving the student attendance history to database
        student_attendance_history = StudentAttendanceHistory.objects.create(
            user_id=request.user.id,
            course=course_details,
            photo_taken=filename
        )
        student_attendance_history.save()
        student_profile_details = StudentProfile.objects.get(user_id=request.user.id)
        if student_profile_details.image is not None:
            known_face = student_profile_details.image.path
        else:
            messages.error(request, 'Please upload a profile photo', extra_tags='warning')
            return render(request, 'attendance/studentAttendance.html')
        status = _compare_faces(known_face=known_face, face_to_check=os.path.join(settings.MEDIA_ROOT,
                                                                                  student_attendance_history.photo_taken))
        # Check if photo matches with the profile photo
        if status:
            # If photo matches with the profile photo, then save the attendance to database
            student_attendance = StudentAttendance.objects.create(
                user_id=request.user.id,
                course=course_details,
                status=True,
            )
            student_attendance.save()
            messages.success(request, 'Attendance marked successfully', extra_tags='success')
        else:
            # If photo does not match with the profile photo, then save the attendance to database
            messages.error(request, 'Attendance not marked', extra_tags='danger')
            return render(request, 'attendance/studentAttendance.html', {'marked': "False",
                                                                         "courses": courses})
        return render(request, 'attendance/studentAttendance.html')
