student_heights = input("Enter a list of student's height: ").split()
total = 0
for n in range(0,len(student_heights)):
  total = int(student_heights[n]) + total   #could use sum function
avg_height = total / len(student_heights)   #could use avg function
print(f"The average height of {len(student_heights)} students is {avg_height}")
