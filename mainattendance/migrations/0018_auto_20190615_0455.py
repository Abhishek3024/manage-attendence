# Generated by Django 2.2.2 on 2019-06-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainattendance', '0017_alldate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentattendance',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentattendance',
            name='student_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
