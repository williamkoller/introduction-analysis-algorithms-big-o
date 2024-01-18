
def logarithm(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(logarithm(my_array, 6))
    print(logarithm(my_array, 10))
    print(logarithm(my_array, 1))


