from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Syllabus(models.Model):
    syllabus_name=models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.syllabus_name

class Day(models.Model):
    days=models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.days

class Task(models.Model):
    task_name=models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.task_name

class Coursetask(models.Model):

    course_Name=models.ForeignKey(Course,on_delete=models.CASCADE)
    Day=models.ForeignKey(Day,on_delete=models.CASCADE)
    Syllabus=models.ManyToManyField(Syllabus)
    Task=models.ManyToManyField(Task)

class CourseSyllabus(models.Model):
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    Day=models.ForeignKey(Day,on_delete=models.CASCADE)
    Syllabus=models.ManyToManyField(Syllabus)



