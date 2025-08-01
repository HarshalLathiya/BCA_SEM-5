def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

y = int(input("Enter a year: "))
if is_leap(y):
    print("It is a leap year.")
else:
    print("It is not a leap year.")
