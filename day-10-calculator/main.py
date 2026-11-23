import art

print(art.logo)

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
    operation = input("+ \n- \n* \n/ \nPick an operation: ")
    second_number = int(input("Type the second number: \n"))
    return operation, second_number

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = int(input("Type the first number: \n"))

# operation = input("+ \n- \n* \n/ \nPick an operation: ")
#
# second_number = int(input("Type the second number: \n"))

operation, second_number = get_operations_inputs()

calculation_function = operations[operation]

result = calculation_function(first_number, second_number)

print(result)

continue_choice = input("Would you like to continue using this result? \n"
                        "Type 'y' to use it again or 'n' to start a new calculation")

if continue_choice == 'y':
    first_number = result
    get_operations_inputs()


