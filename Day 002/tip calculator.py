# Tip Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
total_people = float(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill += (total_bill*tip_percentage)/100
result = round(total_bill / total_people, 2)
print(f"Each person should pay: ${result}")
