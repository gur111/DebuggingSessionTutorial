def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)):
        temp = lst[i]  # Store the current element in a temporary variable
        lst[i] = lst[-(i + 1)]  # Swap the current element with the corresponding one from the end
        lst[-(i + 1)] = temp  # Swap the corresponding element from the end with the temporary variable
    return lst  # Return the reversed list



if __name__ == '__main__':
    print(reverse_list([1, 2, 3, 4, 5, 6]))  # Should print [6, 5, 4, 3, 2, 1]
