# Generated by Django 2.2.2 on 2019-06-08 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainattendance', '0003_currentattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainattendance.Batch'),
        ),
    ]
