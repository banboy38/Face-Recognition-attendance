from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import StudentProfile, Courses, StudentAttendance, StudentAttendanceHistory

# Register your models here.


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    def profile_image_tag(self, obj):
        return mark_safe('<img src="{}" height="50" width="50" />'.format(obj.image.url))
    profile_image_tag.short_description = 'Profile Image'

    list_display = ('user', 'roll_no', 'standard', 'section', 'phone_no', 'address', 'profile_image_tag')
    list_filter = ('standard', 'section')
    search_fields = ('user__username', 'roll_no', 'standard', 'section')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'course_description')
    search_fields = ('course_name', 'course_code')


@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'course', 'status')
    list_filter = ('course', 'status')
    search_fields = ('user__username', 'course__course_name', 'course__course_code')


@admin.register(StudentAttendanceHistory)
class StudentAttendanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'course')
    list_filter = ('course',)
    search_fields = ('user__username', 'course__course_name', 'course__course_code')

