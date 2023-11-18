from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, PreSchool, ExtraClass
from django.views.generic import DetailView


def index(request):
    return render(request, "main/index.html")

def course(request):
    courses = Course.objects.all()
    preSchool = PreSchool.objects.all()
    extraClass = ExtraClass.objects.all()

    context = {
        'courses': courses,
        'preSchool': preSchool,
        'extraClass': extraClass,
    }
    return render(request, "main/course.html", context)


class CourseDetailView(DetailView):
    model = Course
    template_name ='main/one-course.html'
    context_object_name = 'desk'

def about(request):
    return render(request, "main/about.html")

def contatcs(request):
    return render(request, "main/contacts.html")

