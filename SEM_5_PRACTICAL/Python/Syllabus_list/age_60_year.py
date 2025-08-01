from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = datetime.now().year
year_turn = current_year + (60 - age)

print(f"Hello {name}, you will turn 60 in the year {year_turn}.")
