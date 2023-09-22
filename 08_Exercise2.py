# BMI Calculator

print("Hello, This is a BMI Calculator !!!\n")
height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilogram: ")

BMI = int(int(weight) / float(height)**2)
print("Your BMI is: " + str(BMI))