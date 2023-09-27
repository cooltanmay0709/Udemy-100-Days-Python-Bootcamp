# Control Flow Statement

# Nested If-Else Statement
# Syntax - if condition1 : 
#               code block
#               if condition2 :
#                   code block
#               else : 
#                   code block
#          else :
#               code block

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height > 120 :
    print("You are eligible to ride.")
    age = int(input("What's Your Age?\n"))
    if age <= 18 :
        print("Please Pay $7")
    else :
        print("Please Pay $12")
else :
    print("Sorry! You are not eligible to ride.")

# If-Elif-Else Statement
# Syntax - if condition1 : 
#               code block
#          elif condition2 :
#               code block
#          else :
#               code block

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height > 120 :
    print("You are eligible to ride.")
    age = int(input("What's Your Age?\n"))
    if age <= 18 :
        print("Please Pay $7")
    elif age <= 60 :
        print("Please Pay $12")
    else :
        print("Please Pay $5")
else :
    print("Sorry! You are not eligible to ride.")