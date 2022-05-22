from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'fscohort/index.html')

def student_list(request):
    students = Student.objects.all()
    context  = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students')
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)

""" def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students') """
def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("students")
    context = {
        "student": student
    }
    return render(request, "fscohort/student_delete.html",context) 