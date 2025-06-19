print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))/100
people = int(input("How many people to split the bill? "))

to_pay = bill + bill * tip
to_pay_person = to_pay/people
print(f"Each person should pay: {to_pay_person:.2f}")