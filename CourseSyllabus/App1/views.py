from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course,Coursetask,Syllabus,Day,Task

@login_required
def home(request):
    return render(request,'Registration/home.html')


def display_course(request):
    courses = Course.objects.all()
    return render(request, 'Registration/courses.html', {'title': 'Courses', 'data': courses})

def display_syllabus(request):
    syllabuses = Syllabus.objects.all()
    return render(request, 'Registration/syllabus.html', {'title': 'Syllabus', 'data': syllabuses})

def display_task(request):
    tasks=Task.objects.all()
    return render(request,'Registration/task.html',{'title':'Task','data':tasks})


def display_coursetask(request):
    coursetasks=Coursetask.objects.all()
    return render(request,'Registration/coursetask.html',{'title':'course_Tasks','data':coursetasks})

# def display_coursesyllabus(request):
#     coursesyllabus=CourseSyllabus.objects.all()
#     return render(request,'Registration/coursesyllabus.html',{'title':'Course_Syllabus','data':coursesyllabus})
