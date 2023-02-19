def main():
    add_two_numbers(1.5, 2.1)
    subtract_two_numbers(3, 2)
    divide_two_numbers(20, 5)
    multiple_two_numbers(5, 5)


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
