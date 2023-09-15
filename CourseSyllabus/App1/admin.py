from django.contrib import admin
from .models import Course,Syllabus,Task,CourseSyllabus,Day,Coursetask

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','active']

class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['syllabus_name','active']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','active']

class DayAdmin(admin.ModelAdmin):
    list_display = ['days','active']

class CourseSyllabusAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'Day', 'display_syllabuses']
    filter_vertical=['Syllabus']

    def display_syllabuses(self, obj):
        return ", ".join([Syllabus.syllabus_name for Syllabus in obj.Syllabus.all()])
    # display_syllabuses.short_description = 'Syllabuses'

class CourseTaskAdmin(admin.ModelAdmin):
    list_display = ['course_Name', 'Day','display_syllabuses','display_tasks']
    filter_vertical=['Syllabus']
    # filter_vertical=['Task']


    def display_syllabuses(self, obj):
        return ", ".join([Syllabus.syllabus_name for Syllabus in obj.Syllabus.all()])
    # display_syllabuses.short_description = 'Syllabuses'

    def display_tasks(self, obj):
        return ", ".join([Task.task_name for Task in obj.Task.all()])
    # display_tasks.short_description = 'Tasks'

# Register your models here.
admin.site.register(Course,CourseAdmin)
admin.site.register(Syllabus,SyllabusAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Day,DayAdmin)
admin.site.register(CourseSyllabus,CourseSyllabusAdmin)
admin.site.register(Coursetask,CourseTaskAdmin)