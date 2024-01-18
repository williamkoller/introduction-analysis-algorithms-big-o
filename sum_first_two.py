def sum_first_two(arr):
    if len(arr) >= 2:
        return arr[0] + arr[1]
    else:
        return None


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5]
    print(sum_first_two(my_array))
