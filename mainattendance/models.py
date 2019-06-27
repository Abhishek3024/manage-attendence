from django.db import models

# Create your models here.
class Batch(models.Model):
	batch_id = models.CharField(primary_key= True, max_length = 10)
	

	def __str__(self):
		return self.batch_id

class Student(models.Model):
	student_name = models.CharField(max_length = 30)
	student_id = models.IntegerField(primary_key= True, default="")
	batch = models.ForeignKey('Batch', on_delete=models.CASCADE, default="")

	def __str__(self):
		return self.student_name

class Course(models.Model):
	course_id = models.CharField(primary_key= True,max_length = 10)
	course_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.course_name

class CurrentAttendance(models.Model):
	class Meta:
		unique_together = ("date","batch")

	attendance_id = models.AutoField
	date = models.DateField()
	batch = models.CharField(max_length = 10)
	students = models.ManyToManyField(Student, related_name ='student_set')
	
	@classmethod
	def current(cls,date,batch,students):
		current, created = cls.objects.create(
			batch = batch,
			date = date
		)
		current.students.add(students)

	def __str__(self):
		return self.batch

class StudentAttendance(models.Model):
	
	# class Meta:
	# 	unique_together = ("student_id","date","attendance")
	
	attendence_id = models.CharField(primary_key = True)
	student_id = models.CharField(max_length = 10)
	attendance = models.CharField(max_length = 10)
	date = models.DateField()

	def __str__(self):
		return self.student_id+' '+ self.attendance +' '+ str(self.date)

class AllDate(models.Model):
 	date_id = models.AutoField
 	all_date = models.DateField()

 	def __str__(self):
 		return str(self.all_date)

