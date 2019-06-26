from django.contrib import admin
from .models import Batch, Student, Course, CurrentAttendance, StudentAttendance, AllDate
# Register your models here.

admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CurrentAttendance)
admin.site.register(StudentAttendance)
admin.site.register(AllDate)