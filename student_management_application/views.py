from django.shortcuts import render,redirect
from .models import Student, Teacher, Course, Score
from .forms import StudentForm


# Vue pour lister les étudiants
def student_list(request):
    students = Student.objects.all()
    # template = loader.get_template('student_list.html')
    # context = {
    # 'dresses': dresses,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'student_list.html', {'students': students})

# Vue pour lister les cours avec les enseignants associés
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# Vue pour lister les enseignants avec leurs matières respectives
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

# Vue pour lister les scores avec l'information de l'étudiant et du cours pris
def score_list(request):
    scores = Score.objects.all()
    return render(request, 'score_list.html', {'scores': scores})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Rediriger vers la liste des étudiants après ajout
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})