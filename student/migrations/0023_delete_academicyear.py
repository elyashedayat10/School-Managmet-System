# Generated by Django 3.2 on 2022-07-16 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_academicyear'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicYear',
        ),
    ]