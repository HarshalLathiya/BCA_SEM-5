
#if else statement
age = int(input("Enter your age to check you are able for vote or not: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#if – elif – else statement
marks = float(input("Enter your marks to check your grade : "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if statement
num = int(input("Enter a number to check number is negative or positive: "))
if num >= 0:
    print("The number is non-negative")
    if num == 0:
        print("The number is zero") 
    else:
        print("The number is positive")
else:
    print("The number is negative")
