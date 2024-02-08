def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        total = lst[i]
    return total


def average_matrix(matrix):
    lines_sums = []
    for row in matrix:
        line_sum = sum_list(row)
        lines_sums.append(line_sum)

    total = sum_list(lines_sums)
    return total / len(matrix)


if __name__ == '__main__':
    average_matrix([[1, 2], [1, 2]])
    average_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
