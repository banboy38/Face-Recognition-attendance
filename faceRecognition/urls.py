from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.studentProfile, name='profile'),
    path('attendance/', views.studentAttendance, name='attendance'),
    path('show/', views.showAttendance, name='show'),
]