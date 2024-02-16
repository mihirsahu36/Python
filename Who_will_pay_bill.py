import random
print("Welcome to Banker Roulette\n")
name_string = input("Give me everybody name seperated by commas\n")
name = name_string.split(",")
no_of_names = len(name)
person = random.randint(0,no_of_names - 1)
print(f'Today {name[person]} will pay for the bill')
