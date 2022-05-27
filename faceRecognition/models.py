from PIL import Image
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_description = models.TextField()
    course_image = models.ImageField(upload_to='course_image/', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.course_name)

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'


class StudentAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {}'.format(self.user.username, self.time, self.status)

    class Meta:
        unique_together = ('user', 'time')
        ordering = ['-date', '-time']


class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10)
    standard = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='profile_image', null=True)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.user, self.roll_no, self.standard, self.section,
                                          self.phone_no, self.address)

    # Saving the image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # class Meta:
    #     ordering = ['roll_no']


class StudentAttendanceHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    photo_taken = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.user.username, self.time, self.photo_taken)

    class Meta:
        unique_together = ('user', 'time')
        ordering = ['-date', '-time']
