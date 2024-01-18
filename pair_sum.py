def pair_sum(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs


if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
