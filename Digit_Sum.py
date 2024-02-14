num = int(input("Enter the number: "))
num_str = str(num)
num_length = len(num_str)
sum = 0
for i in range(0, num_length):
  sum = sum + int(num_str[i])
print("The indivial digit sum is: " + str(sum))
