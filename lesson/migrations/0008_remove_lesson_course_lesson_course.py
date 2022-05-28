# Generated by Django 4.0.3 on 2022-05-24 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_remove_course_lesson'),
        ('lesson', '0007_lesson_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='course_lesson', to='classroom.course'),
        ),
    ]
