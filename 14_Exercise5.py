# BMI Calculator 2.0

print("Hello, This is a BMI Calculator !!!\n")
height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilogram: ")

BMI = int(int(weight) / float(height)**2)
print("Your BMI is: " + str(BMI))
if BMI < 18.5 :
    print("You are underweight.")
elif BMI < 25 :
    print("You have normal weight.")
elif BMI < 30 :
    print("You are overweight.")
elif BMI < 35 :
    print("You are obese.")
else :
    print("You are clinically obese.")