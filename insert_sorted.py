def insert_sorted(arr, n):
  i = len(arr) - 1
  arr.append(n)
  while i >= 0 and arr[i] > n:
    arr[i + 1] = arr[i]
    i -= 1
  arr[i + 1] = n
  return arr

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(insert_sorted(my_list, 0))