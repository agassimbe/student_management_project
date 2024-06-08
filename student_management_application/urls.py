# student_management_application/urls.py

from django.urls import path
# from .views import student_list, course_list, teacher_list, score_list
from . import views

app_name = 'student_management_application'

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'), 
    path('courses/', views.course_list, name='course_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('scores/', views.score_list, name='score_list'),
]

