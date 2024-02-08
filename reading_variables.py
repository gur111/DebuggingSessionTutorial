def reading_variables():
    # Reading variables
    a = 10
    b = 20
    c = a + b
    total = 0
    for i in range(c):
        print(f"If we don't print i, without a debugger it's hard to track its values")
        total = total + i

    print(f"The total of the first {c} numbers is: {total}")


if __name__ == '__main__':
    reading_variables()
