# Control Flow Statement
# If-Elif-Else Statement
# Syntax - if condition1 : 
#               code block
#          if condition2 :
#               code block
#          if condition3:
#               code block

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? \n"))
bill = 0

if height > 120 :
    print("You are eligible to ride.")
    age = int(input("What's Your Age?\n"))
    if age <= 18 :
        bill = 7
        print("Child Tickets are : $7")
    elif age <= 60 :
        bill = 12
        print("Adults Tickets are : $12")
    else :
        bill= 5
        print("Senior Citizens Tickets are : $5")
    
    want_pics = str(input("Do you want photos of your ride? Yes or No.\n"))
    if want_pics == "Yes" :
        bill += 3
    
    print(f"Your Total Bill is : ${bill}")
else :
    print("Sorry! You are not eligible to ride.")