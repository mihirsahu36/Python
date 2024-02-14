print("Welcome to Tip Calculator\n")
total_bill = float(input("Enter total bill amount: "))
no_people = int(input("Enter the no. of people to split bill: "))
tip = int(input("What percentage of tip you want to give?(10, 12 or 15): "))
bill_with_tip = ((tip/100) * total_bill) + total_bill
bill_split = round((bill_with_tip/no_people),2)
print("Each person should pay: "+ str(bill_split))

  
