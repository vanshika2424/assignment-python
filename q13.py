from datetime import datetime

birth=int(input("Enter birth year: "))

current_year=datetime.now().year

age=current_year-birth

print("My age is",age)