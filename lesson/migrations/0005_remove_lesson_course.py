# Generated by Django 4.0.3 on 2022-05-24 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20220524_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
    ]
