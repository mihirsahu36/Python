print("Your Life in Weeks\n")
curr_age = int(input("Enter your age: "))
expected_age = int(input("Enter your expected age you will live: "))
rem_age = expected_age - curr_age
no_of_days = rem_age * 365
no_of_weeks = rem_age * 52
no_of_months = rem_age * 12
print(f"You have {no_of_days} days, {no_of_weeks} weeks, {no_of_months} months remaining")
