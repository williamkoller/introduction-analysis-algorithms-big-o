def is_valid_solution(board):
    # verify that each row, column, and 3x3 square contains the numbers 1-9
    for row in range(9):
        used_nums = set()
        for col in range(9):
            num = board[row][col]
            if num in used_nums:
                return False
            if num != 0:
                used_nums.add(num)

    # verify that each column contains the numbers 1-9
    for col in range(9):
        used_nums = set()
        for row in range(9):
            num = board[row][col]
            if num in used_nums:
                return False
            if num != 0:
                used_nums.add(num)

    # verify that each 3x3 square contains the numbers 1-9
    for i in range(3):
        for j in range(3):
            used_nums = set()
            for row in range(3):
                for col in range(3):
                    num = board[3*i + row][3*j + col]
                    if num in used_nums:
                        return False
                    if num != 0:
                        used_nums.add(num)
    return True


if __name__ == '__main__':
    board = [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]
    ]
    print(is_valid_solution(board))
