student_marks = input("Enter a list of student's marks: ").split()
for n in range(0, len(student_marks)):
  student_marks[n] = int(student_marks[n])
highest_score = 0
for marks in student_marks:
  if marks > highest_score:       #could use max function
    highest_score = marks

print(f"The highest marks is {highest_score}")
