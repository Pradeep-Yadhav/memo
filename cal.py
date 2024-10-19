def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator(a, b, operation):
    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    elif operation == 'multiply':
        return multiply(a, b)
    elif operation == 'divide':
        return divide(a, b)
    else:
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."

if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 5
    operation = 'add'
    
    result = calculator(num1, num2, operation)
    print(f"Result: {result}")
