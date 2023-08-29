# Your life remaining in years, days, weeks, month
# Assuming that you may live 90 years.
age = input("Please Enter Your Age: ")
age_in_num = int(age)
year_left = 90 - age_in_num
day_left = year_left * 365
weeks_left = year_left * 52
months_left = year_left * 12
print(f"You have {day_left} days, {weeks_left} weeks and {months_left} months left")
