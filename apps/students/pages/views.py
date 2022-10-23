from django.shortcuts import render, redirect, reverse
from apps.students.models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        first_mame = request.POST.get('first_name')
        surname = request.POST.get('surname')
        classs = request.POST.get('class')
        photo = request.FILES.get('photo')

        new_student = Student.objects.create_student(
            first_name=first_mame,
            surname=surname,
            classs=classs
        )
        new_student.photo = photo
        new_student.save()

        # if 'success' in request.session:
        #     del request.session['success']
        # request.session['success'] = True

        return redirect(reverse(students_list))
    return render(request, 'add-student.html')


def scan_student_page(request):
    return render(request, 'scan-profile.html')
