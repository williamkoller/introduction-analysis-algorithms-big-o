def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(n - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

if __name__ == "__main__":
  my_list = [1, 5, 3, 2, 4]
  print(bubble_sort(my_list))