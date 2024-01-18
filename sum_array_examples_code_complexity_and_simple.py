import time


def sum_array_complexity(arr):
    initial = time.time()
    total = 0
    for i in arr:
        total += i
    end = time.time()
    time_elapsed = end - initial
    print(f"Time elapsed: {time_elapsed}")
    return total


def sum_array_simple(arr):
    initial = time.time()

    total = sum(arr)
    end = time.time()
    time_elapsed = end - initial
    print(f"Time elapsed: {time_elapsed}")
    return total


if __name__ == '__main__':
    print(sum_array_complexity([1, 2, 3, 4, 5]))
    print(sum_array_simple([1, 2, 3, 4, 5]))
