def choose_option():
    while True:
        print("\n1. Perform a calculation")
        print("2. Print previous equations")
        print("3. Exit")
        choice = input("Please enter your choice (1, 2, or 3): ")
    
        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            print("Exiting the calculator.")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
def perform_calculation():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation. Please enter one of +, -, *, or /.")
                continue

            print(f"{num1} {operation} {num2} = {result}")
            with open("equations.txt", "a") as file:
                file.write(f"{num1} {operation} {num2} = {result}\n")
            print(choose_option())
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")

def print_previous_equations():
    while True:
        try:
            with open("equations.txt", "r") as file:
                equations = file.readlines()
                if equations:
                    print("Previous equations:")
                    for equation in equations:
                        print(equation.strip())
                    print(choose_option())
                else:
                    print("No previous equations found.")
                    print(choose_option())
        except FileNotFoundError:
            print("No previous equations found. The file does not exist.")
            print(choose_option())

print("Welcome to the Calculator!")
while True:
    choose_option()