# Generated by Django 4.0.3 on 2022-05-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0009_remove_lesson_course'),
        ('classroom', '0006_remove_course_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lesson',
            field=models.ManyToManyField(to='lesson.lesson'),
        ),
    ]
