def evaluating_expressions():
    is_raining = True
    have_umbrella = False
    temperature = int(input("What is the temperature? "))
    cold_threshold = 19

    print("Sometimes it's hard to know why the program didn't enter the `if` block")
    print("The debugger can help us understand why")
    print("We can inspect the values of the variables and even evaluate sub-expressions to see what's going on")

    if is_raining and not have_umbrella and temperature < cold_threshold:
        print("I'm getting wet and sick")
    else:
        print("I'm fine")


if __name__ == '__main__':
    evaluating_expressions()
