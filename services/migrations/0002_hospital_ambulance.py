# Generated by Django 4.1.7 on 2023-04-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='ambulance',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
