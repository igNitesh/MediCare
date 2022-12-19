# Generated by Django 4.1.3 on 2022-12-19 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='beds_avilable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='beds_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='oxygen_cylender_avilable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='oxygen_cylender_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='ventilator_avilable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='ventilator_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.city'),
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
