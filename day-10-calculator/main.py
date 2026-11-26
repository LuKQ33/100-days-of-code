import art


def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference between two numbers (first minus second)."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of dividing the first number by the second."""
    return n1 / n2

def get_operations_inputs():
    """Returns the user inputs operation and second number"""
    for symbol in operations:
        print(symbol)
    operation = input("\nPick an operation: ")
    second_number = float(input("\nType the second number: \n"))
    return operation, second_number

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

should_exit = False
while not should_exit:
    print(art.logo)
    first_number = float(input("Type the first number: \n"))
    should_continue = True
    while should_continue:
        operation, second_number = get_operations_inputs()
        calculation_function = operations[operation]
        result = calculation_function(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        continue_choice = input(f"\nDo you want to continue operating using this result? ( {result} )  \n"
                                "Type 'y' to use it again or 'n' to start a new calculation."
                                " (Type 'exit' to quit): \n")
        if continue_choice == 'y':
            first_number = result
        elif continue_choice == 'n':
            should_continue = False
            print("\n" * 20)
        elif continue_choice == 'exit':
            print('See you next time!')
            should_continue = False
            should_exit = True
