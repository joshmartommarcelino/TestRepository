def calculator(a,b,operation):
    """Performs basic arithmetic operations"""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation"

while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation and display the result
    result = calculator(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")
    
    # Ask user if they want to continue
    continue_choice = input("Do you want to perform another calculation? (yes/no): ")
    if continue_choice.lower() != 'yes':
        print("Thank you for using me~!")
        break