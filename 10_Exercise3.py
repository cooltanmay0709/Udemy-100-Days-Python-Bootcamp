# Life in Weeks
# In this exercise the code should ask your age.
# Consider that you will live for 90 years.
# Output should be your remaining age in weeks, months & days.

print("Hello, Welcome to Life in Weeks !!!")
age = int(input("Enter Your Age: "))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left")
