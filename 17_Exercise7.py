# Automatic Pizza Order Bill

# Pizzas
# Small Pizza : INR 99
# Medium Pizza : INR 199
# Large Pizza : INR 299
# Delivery Charge : INR 39

# Add-on's
# Pepperoni for Small Pizza : INR 20
# Pepperoni for Medium or Large Pizza : INR 30
# Extra Cheese : INR 30

print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L.\n")
add_ons1 = input("Do you want to add pepperoni? Y or N.\n")
add_ons2 = input("Do you want to add extra cheese? Y or N.\n")

bill = 0
if size == "S" :
    bill = 99
    print(f"Cost for Small Pizza is : INR {bill}")
    if add_ons1 == "Y" :
        bill += 20
        print("Add-on Cost for Small Pepperoni : INR 20")
if size == "M" :
    bill = 199
    print(f"Cost for Medium Pizza is : INR {bill}")
    if add_ons1 == "Y" :
        bill += 30
        print("Add-on Cost for Medium or Large Pepperoni : INR 30")
if size == "L" :
    bill = 299
    print(f"Cost for Large Pizza is : INR {bill}")
    if add_ons1 == "Y" :
        bill += 30
        print("Add-on Cost for Medium or Large Pepperoni : INR 30")
if add_ons2 == "Y" :
    bill += 30
    print("Add-on Cost for Extra Cheese : INR 30")

print(f"Your Total Bill : INR {bill}")
print("Thank You!!! Visit Again!!!")


# Alternate Code :
# bill = 0
# if size == "S":
#   bill += 99
#   print(f"Cost for Small Pizza is : INR {bill}")
# elif size == "M":
#   bill += 199
#   print(f"Cost for Medium Pizza is : INR {bill}")
# else size == "S":
#   bill += 299
#   print(f"Cost for Large Pizza is : INR {bill}")
# if add_ons1 == "Y":
#   if size == "S":
#      bill += 20
#      print("Add-on Cost for Small Pepperoni : INR 20")
#   else : 
#      bill += 30
#      print("Add-on Cost for Medium or Large Pepperoni : INR 30")
# if add_ons2 == "S"
#   bill += 30
#   print("Add-on Cost for Extra Cheese : INR 30")
#
# print(f"Your Total Bill : INR {bill}")
# print("Thank You!!! Visit Again!!!")