operations = {}

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero."
    return num1 / num2

operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide



def operation_switch(operation, number, number2):
    if operation == "+":
        return number + number2
    elif operation == "-":
        return number - number2
    elif operation == "*":
        return number * number2
    elif operation == "/":
        return number / number2


def calculator():
    number = float(input("Enter a number: "))
    while True:
        if number == "exit":
            break
        operation = input("Enter an operation. Options are +, -, *, /: ")
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation.")
            continue
        number2 = float(input("Enter another number: "))
        if operation == "/" and number2 == "0":
            print("You can't divide by zero.")
            continue
        output = float(operation_switch(operation, float(number), float(number2)))
        print(f"{number} {operation} {number2} = {output}")
        stop = input("Do you want to continue calculating? Type 'yes' or 'no' to start over. Type 'exit' to quit.\n")
        if stop == "exit":
            exit()
        elif stop == "yes":
            number = output
            continue
        elif stop == "no":
            calculator()


calculator()