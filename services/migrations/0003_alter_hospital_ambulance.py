# Generated by Django 4.1.7 on 2023-04-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_hospital_ambulance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='ambulance',
            field=models.CharField(default='No', max_length=10),
        ),
    ]
