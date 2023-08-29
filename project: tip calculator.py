welcome = "Welcome to tip calculator"
print(welcome)
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage of tip would you like to give? 10, 12 or 15 "))
bill_splitters = int(input("How many people to split the bill? "))
pay_per_person = round((bill + (bill * (tip / 100))) / bill_splitters , 2)
print(f"Each person have to pay ${pay_per_person}")
