from django.shortcuts import render
from student.forms import AddStudentForm
from student.models import Student


# Create your views here.


def add_student(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
            }
        return render(request, "added_student.html", context)
    if request.method == "GET":
        form = AddStudentForm()
        context = {'form': form}
        return render(request, "add_student.html", context)


def home(request):
    return render(request, 'home.html')


def all_students(request):
    student = Student.objects.all()
    context = {
        'students': student
    }
    return render(request, 'all_students.html', context)
