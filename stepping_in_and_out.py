def print_poem():
    # Prints a funny poem related to Python and Monty Python
    print("=" * 50)
    print("Lorem ipsum dolor sit amet, consectetur adipiscing elit,")
    print("sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    print("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris")
    print("nisi ut aliquip ex ea commodo consequat.")
    print("=" * 50)
    return "Done"


def stepping_in_and_out():
    print("When you step over a function call, the debugger would execute the function and stop at the next line")
    print("Let's see an example")
    answer = print_poem()
    print("The answer is:", answer)

    print("If you want to follow the program as it executes the function, you can step into the function")

    another_answer = print_poem()

    print("The answer is:", another_answer)


if __name__ == '__main__':
    stepping_in_and_out()
