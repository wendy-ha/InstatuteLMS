# Generated by Django 4.0.3 on 2022-05-24 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20220523_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lesson',
        ),
    ]
