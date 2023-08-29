h = float(input("Enter your height: "))
w = float(input("Enter your weight: "))
bmi = round(w / h ** 2, 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi > 18.5 and  bmi < 25:
    print(f"Your bmi is {bmi}, you have normal weight")
elif bmi < 25 and bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")

