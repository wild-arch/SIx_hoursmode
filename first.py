#name = input("What is your name? ")
from operator import length_hint

#print('hi ' + name + '!')

 #learn about type conversion
#birth_year = input("When were you born? ")
#print(type(birth_year))
#age = 2025 - int(birth_year)
#print(type(age))
#print("Mike, you must be  ", age,  " years old!")


# Technical question

#weight_pounds = input("What is your weight in pounds? ")

#weight_kg = float(weight_pounds) * 0.45359237

#print("You weigh ", weight_kg, " kilograms.")

#msg = '''
#dear mike,

#you are the f* best!
#sincerely,
#your biggest fan
#mike


good_credit = True
price = 1000000
if good_credit:
    down_payment = (price/100) * 10
    print(f"${down_payment}" )
else:
    down_payment = (price/100) * 20
    print(f"${down_payment}" )

name = input("What is your name? ")
if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name must be less than 50 characters long.")
else:
    print("Name is okay.")

