# Generated by Django 2.2.2 on 2019-06-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainattendance', '0008_currentattendance_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentattendance',
            name='students',
            field=models.ManyToManyField(related_name='student_set', to='mainattendance.Student'),
        ),
    ]