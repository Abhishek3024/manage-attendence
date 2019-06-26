from django.shortcuts import render
from mainattendance.models import StudentAttendance,CurrentAttendance,Batch,Student
# Create your views here.
def page(request):
	# batchs = CurrentAttendance.objects.values('batch','date')
	# if request.method == "GET":
	# 	xbatch = request.GET.get('batch')

	# params = {'batchs':batchs}
	# if xbatch is not None:
	# 	sbatch = xbatch.split(' on ')
	# 	batch = sbatch[0]
	# 	date = sbatch[1]		
	# 	xstudents = CurrentAttendance.objects.get(batch=batch,date=date)
		
	# 	astudents = xstudents.students.all()
	# 	no_of_students =astudents.count()

	# 	att_list = []
	# 	for a in range(0,no_of_students):
	# 		at = StudentAttendance.objects.get(student_id = astudents[a].student_id,date=date)
	# 		att_list.append(at)

	# 	print(att_list)
	# 	params = {'xattendance':att_list,'date':date}

	batchs = Batch.objects.all()
	params={'batchs': batchs}
	if request.method == "GET":
		xbatch = request.GET.get('batch')
		xdates = CurrentAttendance.objects.filter(batch = xbatch)
		

		no_of_dates = xdates.count()
		# print(no_of_dates)
		att_list = []
		for a in range(0,no_of_dates):
			print(xdates[a].date)

			xstudents = CurrentAttendance.objects.get(batch =xbatch, date= xdates[a].date)
			astudents= xstudents.students.all()
			no_of_students = astudents.count()

			# cdate = xdates[a].date
			for i in range(0,no_of_students):
				print(astudents[i].student_id)

				at = StudentAttendance.objects.get(student_id = astudents[i].student_id,date = xdates[a].date)
				# print(at)
				att_list.append(at)


		print(att_list)

		params={'xattendance':att_list}
	return render(request, 'viewattendance/page.html',params)	
