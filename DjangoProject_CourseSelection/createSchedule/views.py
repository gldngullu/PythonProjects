from .models import Course, Student
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# superuser: gldng password: sadece123
# user: mertali password: sadece123123

@login_required
def available_courses(request):
    loggedUser = request.user
    takenCourses = Course.objects.filter(student__user_id=loggedUser.id)
    availableCourses = Course.objects.exclude(id__in=takenCourses)
    return render(request, 'createSchedule/available_courses.html', {'courses': availableCourses})


@login_required
def local_users(request):
    students = Student.objects.all()
    return render(request, 'createSchedule/profile.html', {'students': students})


@login_required
def main_page(request):
    return render(request, 'createSchedule/main_page.html')


@login_required
def schedule(request):
    loggedUser = request.user
    takenCourses = Course.objects.filter(student__user_id=loggedUser.id)
    return render(request, 'createSchedule/schedule.html', {'courses': takenCourses})



