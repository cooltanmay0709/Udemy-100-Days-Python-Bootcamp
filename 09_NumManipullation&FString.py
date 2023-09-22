# Number Manipulation and F String

# Rounding up numbers
print(8 / 3) # Standard Division Without Rounding Up
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.68699143, 2))
print(8 // 3)

# More about number manipulation
result = 4 / 2
result /= 2
print(result)

score = 0
score += 1
print("Your score is: " + str(score))

weight = 60
height = 1.6764
isUnderWeight = False
# f-String
print(f"Your Weight is: {weight}, Your Height is: {height}, Are You Underweight: {isUnderWeight}")