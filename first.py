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



    # weight converter

weight = input("What is your weight? ")
weight = int(weight)
pounds = weight * 0.45
grams = weight * 2.20

print("(L)bs or (K)g? ")
if input().lower() == "l":
    print(f"You weigh {pounds} kilograms.")
else:
    print(f"You weigh {grams} pounds.")

