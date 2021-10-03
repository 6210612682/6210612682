from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

from .models import Course
from users.views import *

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })


def course(request, c_id):
    course = get_object_or_404(Course, pk=c_id)
    student_count = course.students.all().count()
    status = course.status
    if request.user.is_superuser:
        return render(request, "courses/course_admin.html", {
        "course": course,
        "students": course.students.all(),
        "student_count": student_count,
        "status": status,
        })
    else:
        return render(request, "courses/course.html", {
        "course": course,
        "students": course.students.all(),
        "student_count": student_count,
        })


def books(request, c_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    course = get_object_or_404(Course, pk=c_id)
    if request.user not in course.students.all():
        if course.students.all().count() < course.vacancy and course.status == "OPEN":
            course.students.add(request.user)


    return HttpResponseRedirect(reverse("courses:course", args=(c_id,)))


def cancel_enrollment(request, c_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    course = get_object_or_404(Course, pk=c_id)
    if request.user in course.students.all():
        course.students.remove(request.user)


    return HttpResponseRedirect(reverse("courses:course", args=(c_id,)))

