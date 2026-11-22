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

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = int(input("Type the first number: \n"))

operation = input("+ \n- \n* \n/ \nPick an operation: ")

second_number = int(input("Type the second number: \n"))

result = operations[operation]

print(result(first_number, second_number))
