# Type Error, Type Checking and Type Conversion

# Part 1 -
#Type Error
# len(4434)
# In the above line it gives type error as the len() function does not work with integers.

# Part 2 -
#Type Error
num = len(input("What is your name?\n"))
# print("Your name has " + num_char + " characters.")
# Above code gives type error : we can only concatenate str (and 'int') to str.

# Part 3-
# Type Checking : Checking the type of the data
print(type(num))

# Part 4 - 
# Type Conversion
# The error in the part 2 can be rectified by type conversion.
num_char = str(num)
print("Your name has " + num_char + " characters")
print(type(num_char))

# Examples of Type Conversion
print(70 + float("73"))
print(str(14) + str(3))