from django.shortcuts import render
from .models import Batch, CurrentAttendance, Student, StudentAttendance, AllDate
# Create your views here.

def home(request):
	batchs = Batch.objects.all();
	params = {'batchs':batchs}

	if request.method == "POST":
		date = request.POST.get('date','')
		batch = request.POST.get('batch','')
		
		students = Student.objects.filter(batch=batch)
		instance = CurrentAttendance.objects.create(batch=batch, date=date)

		alldate = AllDate(all_date = date)
		alldate.save()
	
		print(alldate)

		instance.students.set(students)

		params = {'date':date, 'batch':batch, 'students':students}
	return render(request,'mainattendance/main.html',params)

def start(request):
	n = CurrentAttendance.objects.count()
	attendance = CurrentAttendance.objects.all()[n-1]
	date = attendance.date
	batch = attendance.batch
	students = attendance.students.all()
	if request.method == "GET":
		attendance = request.GET.get('attendance')
		if attendance is not None:
			main = attendance.split('-')
			if main[0] == "ab":
				value = 'Absent'
			else:
				value = 'Present'

			student_id = main[1]

			studentattendance = StudentAttendance(student_id = student_id, attendance = value, date = date)
			studentattendance.save()


	attstudents = StudentAttendance.objects.filter(date = date)
	
	params = {'date':date, 'batch':batch, 'students':students, 'attstudents':attstudents }
	

	return render(request,'mainattendance/Start.html',params)