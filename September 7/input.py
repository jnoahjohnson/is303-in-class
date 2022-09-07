# Description: Using input in Python
# Author: Noah Johnson

# The input function is used to get input from the user
# The input function returns a string
# The input function takes an optional argument which is the prompt
# The input function syntax is:
# input([prompt])

# Example: Getting input from the user
name = input("What is your name? ")
print("Hello " + name)

# Data conversion
# The input function returns a string
# If you want to use the input as a number, you need to convert it
# The int function converts a string to an integer
# The float function converts a string to a float
# The str function converts a number to a string
# The int and float functions take one argument which is the string to convert
# The str function takes one argument which is the number to convert
# The int and float functions syntax is:
# int(string)
# float(string)
# The str function syntax is:
# str(number)

userAge = input("What is your age? ")
# Note: Remember how we talked about how Python is a dynamically typed language?
# That means that you don't have to declare the type of a variable
# Python will figure out the type of the variable for you
userAge = int(userAge)
print(userAge)

# Example: Getting input from the user and converting it to an integer
age = int(input("What is your age? "))
print("You are " + str(age) + " years old")

# Another Example
userAge = int(input("How old are you? "))
newAge = userAge + 1
print("In one year you will be...", newAge, ".")
