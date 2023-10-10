# HW2.py
# Author:


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
input = int(input("Enter your age: "))
if input < 13:
    print("You are a child.")
elif input >= 13 and input <= 19:
    print("You are a teenager.")
elif input >= 20:
    print("You are an adult.")
# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.

# Initialize variables for highest, lowest, and sum
highest = 0
lowest = 0
sum = 0
# Prompt user for 10 numbers
for i in range(1,11):
    num = int(input("Enter a number: "))
    # Check if the number is the highest or lowest
    if i == 1:
        highest = num
        lowest = num
    elif num > highest:
        highest = num
    elif num < lowest:
        lowest = num
    # Add the number to the sum
    sum += num
# Calculate the average
average = sum / 10
# Display the highest, lowest, and average
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Average: ",average)


# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement
string = str(input("Enter a string: ")).lower()
count = 0
for i in string:
    if i in "aeiou":
        count += 1
print("The number of vowels in the string is: ",count)

