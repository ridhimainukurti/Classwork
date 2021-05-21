# Calculator Code - Iniyaa's Project

# addition function
def addition(x, y):
    return x + y


# subtraction function
def subtraction(x, y):
    return x - y


# multiplication function
def multiplication(x, y):
    return x * y


# division function
def division(x, y):
    return x / y


print("Choose Mathematic Operation")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")


while True:
    choice = input("enter the number that corresponds with the operation you want the calculator to perform")

    if choice in ('1',)