# HW1.py
# Author:

# Question 1:
# Print Hello World like we did in class
print ("question 1:")
print ("Hello World")
# Question 2:
# Print the following:
# Your name
print ("question 2:")
print ("John Fernan")
# Your age
print ("18")
# Your favorite color
print ("grey")
# Your favorite animal
print ("dog")
# Question 3:
# Create a variable called "myName" and set it equal to your name
print ("question 3:")
myName = "John Fernan"
# Create a variable called "myAge" and set it equal to your age
myAge = "18"
# Create a variable called "myColor" and set it equal to your favorite color
myColor = "grey"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "dog"
# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>
print ("Hello, my name is " + myName)
print ("I am " + myAge + " years old")
print ("My favorite color is " + myColor) 
print ("My favorite animal is " + myAnimal)


# Question 4:
# Calculate the following and print the result:
print ("question 4:")
# 2 + 2
print (2 + 2)
# 3 * 4
print (3 * 4)
# 5 - 6
print (5 - 6)
# 8 / 2
print (8 / 2)
# Question 5:
print ("question 5:")
# Create a variable called "num1" and set it equal to 2
num1 = 2
# Create a variable called "num2" and set it equal to 3
num2 = 3
# Create a variable called "num3" and set it equal to 4
num3 = 4
# Create a variable called "num4" and set it equal to 5
num4 = 5
# Calculate the following and print the result:
# num1 + num2
print (num1 + num2)
# num3 * num4
print (num3 * num4)
# num4 - num1
print (num4 - num1)
# num2 / num1
print (num2 / num1)
# Question 6: Write a program that asks the user for their name and then prints the following:
print ("question 6:")
name1 = input ("What is your name?")
# Hello, <name>. Please enter three numbers.
print ("Hello, "+name1+". Please enter three numbers.")
num1 = input ("What is your first number?")
num2 = input ("What is your second number?")
num3 = input ("What is your third number?")
float (num1)
float (num2)
float (num3)
#input ("Hello, "+name+". Please enter three numbers.") = num1, num2, num3
# The program should then ask the user for three numbers (floats) and print the following:


# 1. The sum of the three numbers is <sum>
print ("The sum of the three numbers is " + str(float(num1) + float(num2) + float(num3)))
# 2. The product of the three numbers is <product>
print ("The product of the three numbers is " + str(float(num1) * float(num2) * float(num3)))
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 
print ("The sum of the three rounded numbers divided by 3 is " + str(round(float(num1)) + round(float(num2)) + round(float(num3)) / 3))
# 4. The average of the three numbers is <average>
print ("The average of the three numbers is " + str((float(num1) + float(num2) + float(num3)) / 3))
# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
print ("question 7:")
symbol = input ("What symbol would you like to use?")
print ("    " + symbol + "     |")
print ("   " + symbol + symbol + symbol + "    |")
print ("  " + symbol + symbol + symbol + symbol + symbol + "   |")
print (" " + symbol + symbol + symbol + symbol + symbol + symbol + symbol + "  |")
print (" " + symbol + symbol + symbol + symbol + symbol + symbol + symbol + "  |")
print ("  " + symbol + symbol + symbol + symbol + symbol + "   |")
print ("   " + symbol + symbol + symbol + "    |")
print ("    " + symbol + "     |")

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
