from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home),
    path('display/course/', views.display_course, name='display_course'),
    path('display/syllabus/', views.display_syllabus, name='display_syllabus'),
    path('display/task/',views.display_task,name='display_task'),
    path('display/coursetask',views.display_coursetask,name='display_coursetask'),
    # path('display/coursesyllabus',views.display_coursesyllabus,)
    
]
