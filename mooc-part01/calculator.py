number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
operation = input("What operation? ")
if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
elif operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")
