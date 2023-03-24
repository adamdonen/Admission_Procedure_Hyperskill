# write your code here
import math
import statistics
from _ast import Lambda


num_department_accepted = int(input())
file = open("applicants.txt", "r")
a = file.read()
a = a.split('\n')
lst = []
s = set()
for elm in a:
	lst.append(elm.split())
	s.add(elm.split()[7])
	s.add(elm.split()[8])
	s.add(elm.split()[9])

lst.sort(key=lambda x: (-int(x[2]), -int(x[3]), -int(x[4]), -int(x[5]), x[0], x[1], x[7], x[8], x[9]))

for el in lst:
	el.append(True)
	el.append(0.0)
s = sorted(s)
applicants = []
accepted_per_department = {dep: [[], True] for dep in s}

flag = False
full = False

check_departments = 0
prevStudent = None
pri = -1
count = 0
meanFlag = False
while pri < 3:
	pri += 1
	for department in s:
		index = 0
		index2 = 0
		mean = 0.0
		tempList = []
		for student in lst:
			if student[len(student) - 2] and student[7+pri] == department:
				if department == "Chemistry":
					a = student[3]
					b = student[6]
					if b > a:
						student[3] = b
						student[11] = a
					meanFlag= False
				elif department == "Mathematics":
					a = student[4]
					b = student[6]
					if b > a:
						student[4] = b
						student[11] = a
					meanFlag = False
				else:
					meanFlag = True
					if department == "Biotech":
						index = 3
						index2 = 2
						# mean = (float(student[index]) + float(student[index2])) / 2.0
						mean = statistics.mean(((float(student[index]), float(student[index2]))))
						if float(student[6]) > mean:
							student[11] = student[6]
						else:
							student[11] = mean
					elif department == "Physics":
						index = 2
						index2 = 4
						mean = statistics.mean(((float(student[index]), float(student[index2]))))
						if float(student[6]) > mean:
							student[11] = student[6]
						else:
							student[11] = mean
					elif department == "Engineering":
						index = 4
						index2 = 5
						mean = statistics.mean(((float(student[index]), float(student[index2]))))
						if float(student[6]) > mean:
							student[11] = student[6]
						else:
							student[11] = mean
				tempList.append(student)
		if meanFlag:
			lst.sort(key=lambda x: (-float(x[11]), x[0], x[1], x[7], x[8], x[9]))
			tempList.sort(key=lambda x: (-float(x[11]), x[0], x[1], x[7], x[8], x[9]))
			meanFlag = False
		else:
			if department == "Chemistry":
				lst.sort(key=lambda x: (-float(x[3]), -float(x[6]),  x[0], x[1], x[7], x[8], x[9]))
				tempList.sort(key=lambda x: (-float(x[3]),  x[0], x[1], x[7], x[8], x[9]))
			elif department == "Mathematics":
				lst.sort(key=lambda x: (-float(x[4]), x[0], x[1], x[7], x[8], x[9]))
				tempList.sort(key=lambda x: (-float(x[4]), x[0], x[1], x[7], x[8], x[9]))
		for student in tempList:
			if student[len(student) - 2]:
				if len(accepted_per_department[department][0]) == num_department_accepted:
					flag = True
					accepted_per_department[department][1] = False
					break
				elif student[7 + pri] == department and len(accepted_per_department[department][0]) != num_department_accepted:
					accepted_per_department[department][0].append(student)
					prevStudent = student
					index = lst.index(prevStudent)
					lst[index][len(student) - 2] = False
					prevStudent = None

for elm in accepted_per_department:
	index = 0
	if elm == "Chemistry":
		index = 3
		accepted_per_department[elm][0].sort(key=lambda x: (-float(x[index]), x[0], x[1]))
	elif elm == "Physics":
		index = 2
		accepted_per_department[elm][0].sort(key=lambda x: (-float(x[11]), x[0], x[1]))
	elif elm == "Biotech":
		index = 3
		accepted_per_department[elm][0].sort(key=lambda x: (-float(x[11]), x[0], x[1]))
	elif elm == "Mathematics":
		index = 4
		accepted_per_department[elm][0].sort(key=lambda x: (-float(x[index]), x[0], x[1]))
	elif elm == "Engineering":
		index = 5
		accepted_per_department[elm][0].sort(key=lambda x: (-float(x[11]), x[0], x[1]))

	print(f"{elm}")
	newFile = open(f"{elm.lower()}.txt", 'w')
	for stud in accepted_per_department[elm][0]:
		if elm == "Chemistry" or elm == "Mathematics":
			newFile.write(f"{stud[0]} {stud[1]} {float(stud[index])} \n")
			print(f"{stud[0]} {stud[1]} {float(stud[index])}")
		else:
			newFile.write(f"{stud[0]} {stud[1]} {stud[11]} \n")
			print(f"{stud[0]} {stud[1]} {stud[11]}")
	print('\n')
	newFile.close()

file.close()
