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





# car game
help = """
Welcome to the car game!
start - Start the car
stop - Stop the car
quit - Quit the game
"""
quit = False

while True:
    command = input(">").lower()
    if command == "help":
        print(help)
    elif command == "start":
        print("Car started... Ready to go!")
    elif command == "stop":
        print("Car stopped.")
    elif command == "quit":
        print("Game over.")
        break
    else:
        print("I don't understand that command.")