total_sum_even = 0
total_sum_odd = 0
for i in range(0, 101):    #could also use range(0, 101, 2)
  if i % 2 == 0:
    total_sum_even = i + total_sum_even
for i in range(0, 101):    #could also use range(0, 101, 1)
  if i % 2 != 0:
    total_sum_odd = i + total_sum_odd

print(f'Sum of even number between 0 to 100 is {total_sum_even}')
print(f'Sum of odd number between 0 to 100 is {total_sum_odd}')
