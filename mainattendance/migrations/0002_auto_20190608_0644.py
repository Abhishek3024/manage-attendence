# Generated by Django 2.2.2 on 2019-06-08 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainattendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='batch',
            name='batch_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.ForeignKey(default='CS2016', on_delete=django.db.models.deletion.CASCADE, to='mainattendance.Batch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=201651003, primary_key=True, serialize=False),
        ),
    ]
