def permutations(arr):
    if len(arr) == 0:
        return [[]]
    else:
        total = []
        for i in range(len(arr)):
            remaining_elements = arr[:i] + arr[i+1:]
            sub_permutations = permutations(remaining_elements)
            for permutation in sub_permutations:
                total.append([arr[i]] + permutation)
        return total

if __name__ == "__main__":
    my_list = [1, 2, 3]
    print(permutations(my_list))
