print("BMI Calculator\n")
height = float(input("Enter your height(in m): "))
weight = float(input("Enter your weight(in kg): "))
BMI = weight/height**2
if BMI <= 18.5:
  print("Your BMI is " + str(BMI) + "\nYou are UNDERWEIGHT")
elif BMI > 18.5 and BMI <=24.9:
  print("Your BMI is " + str(BMI) + "\nYou are NORMALWEIGHT")
if BMI > 24.9:
  print("Your BMI is " + str(BMI) + "\nYou are OVERWEIGHT")
