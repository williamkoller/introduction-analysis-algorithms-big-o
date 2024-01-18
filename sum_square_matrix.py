def sum_square_matrix(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        for j in range(n):
            total += matrix[i][j]
    return total


if __name__ == '__main__':
    my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sum_square_matrix(my_matrix))
