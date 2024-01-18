import time


def sum_number_complexity(N):
    initial = time.time()
    result: int = 0
    for i in range(1, N + 1):
        result += i

    end = time.time()

    time_elapsed = end - initial
    print(f"Time elapsed: {time_elapsed}")
    return result


def sum_numbers_simple(N):
    initial = time.time()
    result = N * (N + 1) // 2

    end = time.time()
    time_elapsed = end - initial
    print(f"Time elapsed: {time_elapsed}")
    return result


if __name__ == '__main__':
    print(sum_number_complexity(100))
    print(sum_numbers_simple(100))
