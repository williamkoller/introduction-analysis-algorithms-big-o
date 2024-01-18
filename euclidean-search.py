def euclidean_search(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print(euclidean_search(30, 18))
