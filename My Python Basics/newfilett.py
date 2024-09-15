

total_marks=0
for marks in (0, 99+1):
	total_marks += marks
	break
average=total_marks/len(marks)
print("total marks are: ", average)