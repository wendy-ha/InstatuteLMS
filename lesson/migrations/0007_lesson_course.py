# Generated by Django 4.0.3 on 2022-05-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_remove_course_lesson'),
        ('lesson', '0006_auto_20220524_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(to='classroom.course'),
        ),
    ]
