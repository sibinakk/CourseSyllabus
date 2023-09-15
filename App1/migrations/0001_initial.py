# Generated by Django 4.2.4 on 2023-09-01 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coursetask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.day')),
                ('Syllabus', models.ManyToManyField(to='App1.syllabus')),
                ('Task', models.ManyToManyField(to='App1.task')),
                ('course_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSyllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.day')),
                ('Syllabus', models.ManyToManyField(to='App1.syllabus')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.course')),
            ],
        ),
    ]