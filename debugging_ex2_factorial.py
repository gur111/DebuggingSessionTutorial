def factorial(n):
    total = 1
    for i in range(n):
        total *= i
    return total


if __name__ == '__main__':
    result = factorial(5)
    print(f"The factorial of 5 is: {result}")
