# Generated by Django 4.2 on 2023-05-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_hospital_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]