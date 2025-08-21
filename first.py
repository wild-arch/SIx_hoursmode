def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("its an even number")
    else:
        print("its an odd number")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

main()