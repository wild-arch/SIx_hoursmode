# lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 79, 2029, 1000]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print("The maximum number is:", max)