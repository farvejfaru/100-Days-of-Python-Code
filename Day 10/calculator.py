from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def is_valid_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def calculator():
    print(logo)
    print("Welcome to the calculator!")
    continue_program = True

    while continue_program:
        num1 = input("What is the first number?: ")

        if not is_valid_number(num1):
            print("Invalid input. Please enter a valid number.")
            continue
        num1 = float(num1)

        continue_calculation = True
        while continue_calculation:
            print("\nAvailable operations:")
            for symbol in operations:
                print(symbol)

            operation_symbol = input("Choose the operation: ")
            if operation_symbol not in operations:
                print("Invalid operation. Please select a valid operation.")
                continue

            num2 = input("Enter the next number: ")
            if not is_valid_number(num2):
                print("Invalid input. Please enter a valid number.")
                continue
            num2 = float(num2)

            result = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")

            choice = input(f"\nType 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
            if choice == "y":
                num1 = result
            elif choice == "n":
                continue_calculation = False  
            else:
                print("Invalid choice. Starting a new calculation.")
                continue_calculation = False

        exit_choice = input("Do you want to exit the calculator? Type 'yes' to exit or any other key to continue: ").lower()
        if exit_choice == "yes":
            continue_program = False

    print("Thank you for using the calculator. Goodbye!")

calculator()
