import random

letters = []
for c in range(97, 123):
  letters.append(chr(c))
for c in range(65, 91):
  letters.append(chr(c))
  
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How amny letters you want in your password?"))
no_numbers = int(input("How amny numbers you want in your password?"))
no_symbols = int(input("How amny symbols you want in your password?"))

password_list = []
for char in range(1, no_letters + 1):
  password_list += random.choice(letters)

for char in range(1, no_numbers + 1):
  password_list += random.choice(numbers)

for char in range(1, no_symbols + 1):
  password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in (password_list):
  password += char

print(f'Your password is {password}')
