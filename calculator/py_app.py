# Define add, sub, mul, div
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2 if num1 > num2 else num2 - num1

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2 if num1 > num2 else num2 / num1
while True:
    num1 = int(input("Type first number: "))
    num2 = int(input("Tepe second number: "))
    operator = input("Witch operation do you want? (+, -, *, /, e = exit)")

    if operator == "+":
        print(add(num1, num2))
    elif operator == "-":
        print(sub(num1, num2))
    elif operator == "*":
        print(mul(num1, num2))
    elif operator == "/":
        print(div(num1, num2))
    elif operator == "e" or operator == "E":
        quit() 

