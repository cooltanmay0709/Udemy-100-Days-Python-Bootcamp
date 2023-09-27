# To Check For Leap Year
# on every year that is evenly divisible by 4.
#  except every year that is evenly divisible by 100.
#   unless the year is also evenly divisible by 400.

print("Welcome To The Coding Exercise!")
year = int(input("Which year do you want to check?\n"))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print(f"{year} is a leap year.")
        else :
            print(f"{year} is not a leap year.")
    else :
        print(f"{year} is not a leap year.")
else :
    print(f"{year} is not a leap year.")