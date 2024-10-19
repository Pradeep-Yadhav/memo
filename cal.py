def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()