def moving_cursor_around():
    print("We sometimes (under certain conditions) want to move the execution to a specific line.")
    print("This can be useful when we have a problematic code that we don't want or can't fix right now")
    print("and we want to see how the code after it runs")

    print("The following line would crash the program")
    zero = 0
    print(1 / zero)
    print("This line would never be executed")
    print("We can also move the cursor to skip some cumbersome operation that either ",
          "takes time or not relevant to the part of the code we are interested in")
    user_input = input("Enter a number: ")
    print(f"The input is: {user_input}")

    total = 0
    for i in range(1000000):
        total += i

    print(f"The total is: {total}")
    print("Goodbye!")


if __name__ == '__main__':
    moving_cursor_around()
