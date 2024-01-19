def cubic_complexity_algorithm(n):
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += 1
    return total


if __name__ == "__main__":

    size = 3  # You can adjust the size as needed
    result = cubic_complexity_algorithm(size)
    print(f"Result for n={size}: {result}")
