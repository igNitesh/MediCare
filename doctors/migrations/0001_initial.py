# Generated by Django 4.1.7 on 2023-04-11 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0004_alter_hospital_ambulance'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hospital', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
                ('availability_time', models.CharField(max_length=15)),
                ('availability_on', models.CharField(max_length=15)),
                ('fee', models.CharField(max_length=30)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctors.department')),
            ],
        ),
    ]
