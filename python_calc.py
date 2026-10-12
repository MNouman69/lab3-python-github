def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        return a / b

def even_odd(x):
    if (x != int(x)):
        print(f"{x} is not a whole number, so it is neither even nor odd.")
    elif (x % 2 == 0):
        print(f"{int(x)} is an even number.")
    else:
        print(f"{int(x)} is an odd number.")

def percentage(x, y):
    if y == 0:
        print("Error: Dividing by zero is not allowed.")
    else:
       return (x / y) * 100

def exit_program():
    print("You have successfully left the program.")

def calculations():
    i = 0
    while i != 7:
        print("\n         Calculator-Menu         ")
        print("Enter 1 for adding two number.")
        print("Enter 2 for subtracting two number.")
        print("Enter 3 for multiplying two number.")
        print("Enter 4 for dividing two number.")
        print("Enter 5 for checking if numbers are even or odd.")
        print("Enter 6 for calculating percentage.")
        print("Enter 7 to exit the program.")

        i = int(input("Enter your choice: "))

        if i == 1:
            print("Performing addition operation:")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"The addition of numbers {a} and {b} is {addition(a, b)}.")

        elif i == 2:
            print("Performing subtraction operation:")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"The subtraction of numbers {a} and {b} is {subtraction(a, b)}.")

        elif i == 3:
            print("Performing multiplication operation:")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"The multiplication of numbers {a} and {b} is {multiplication(a, b)}.")

        elif i == 4:
            print("Performing division operation:")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = division(a, b)
            if result is not None:
                print(f"The division of numbers {a} and {b} is {result}.")

        elif i == 5:
            print("Performing even/odd operations:")
            x = float(input("Enter the number: "))
            even_odd(x)

        elif i == 6:
            print("Finding percentage of a number:")
            x = float(input("Enter the numerator: "))
            y = float(input("Enter the denominator/whole-part: "))
            result = percentage(x, y)
            if result is not None:
                print(f"The percentage is {result}.")

        elif i == 7:
            exit_program()
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

calculations()
