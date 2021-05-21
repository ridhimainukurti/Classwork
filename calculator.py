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

    if choice in ('1','2','3','4'):
        firstnum = float(input("Type the first number"))
        secondnum = float(input("Type the second number"))

        if choice == '1':
            print("sum = ", addition(firstnum, secondnum))

        elif choice == '2':
            print("difference = ", subtraction(firstnum, secondnum))

        elif choice == '3':
            print("ptoduct = ", multiplication(firstnum, secondnum))

        elif choice == '3':
            print("quotient = ", division(firstnum, secondnum))
    else:
        print("Please enter 1,2,3, or 4 for the operation you want the calculator ot perform")

