

"""
This file helps demonstrates the debugger's basic ability to step through code following the computers execution
"""

def basic_stepping():
    print("This is the main function")
    print("The highlighted line is the next line to be executed")
    print("Clicking resume would execute until the next breakpoint")
    print("The debugger wouldn't stop before this line")
    print("Neither it would stop before running this line")
    print("It would stop right after this line, before running the next line")
    print("The debugger would stop here")

    print("Let's look at a loop now")
    for i in range(5):
        print("The value of i is: ", i)
        print("The debugger would stop each time we reach this line")

    for j in range(5):
        print("The value of j is: ", j)
        print("Stepping 'over' line-by-line would bring us to the for's beginning because that the next line to be executed")


if __name__ == '__main__':
    basic_stepping()
