from django.shortcuts import render
from .models import Student, Teacher, Course, Score

# Vue pour lister les étudiants
def student_list(request):
    students = Student.objects.all()
    return render(request, 'templates/student_list.html', {'students': students})

# Vue pour lister les cours avec les enseignants associés
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'templates/course_list.html', {'courses': courses})

# Vue pour lister les enseignants avec leurs matières respectives
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'templates/teacher_list.html', {'teachers': teachers})

# Vue pour lister les scores avec l'information de l'étudiant et du cours pris
def score_list(request):
    scores = Score.objects.all()
    return render(request, 'templates/score_list.html', {'scores': scores})
