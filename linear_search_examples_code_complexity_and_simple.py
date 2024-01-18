def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5]
    print(linear_search(my_array, 4))
    print(linear_search(my_array, 6))
