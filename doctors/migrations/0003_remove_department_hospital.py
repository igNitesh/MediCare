# Generated by Django 4.1.7 on 2023-04-11 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='hospital',
        ),
    ]
