def main():
    a = 0
    b = 0

    a, b = get_values()
    add_two_numbers(a, b)

    a, b = get_values()
    subtract_two_numbers(a, b)

    a, b = get_values()
    divide_two_numbers(a, b)

    a, b = get_values()
    multiple_two_numbers(a, b)

    
def get_values():
    a = 0
    b = 0
    a: float = float(input("Enter a: "))
    b: float = float(input("Enter b: "))
    return a, b


def add_two_numbers(a, b):
    result = a + b
    print(f"{a} + {b} =", result)


def subtract_two_numbers(a, b):
    result = a - b
    print(f"{a} - {b} =", result)


def divide_two_numbers(a, b):
    result = a / b
    print(f"{a} / {b} =", result)


def multiple_two_numbers(a, b):
    result = a * b
    print(f"{a} * {b} =", result)


main()
