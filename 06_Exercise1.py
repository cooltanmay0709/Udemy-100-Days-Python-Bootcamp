# Write a code that takes 2 digit input number.
# If the input number is 69
# Then write a code that gives output as 6 + 9 = 15

num = input("Enter a two digit number: ")
char1 = num[0]; # Subscripting
char2 = num[1]; # Subscripting
out = int(char1) + int(char2)
print("Output: " + str(out))