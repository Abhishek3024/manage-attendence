# Generated by Django 2.2.2 on 2019-06-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainattendance', '0002_auto_20190608_0644'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('batch', models.CharField(max_length=10)),
            ],
        ),
    ]
