def find_min_max(arr):
  n = len(arr)
  min_val = max_val = arr[0]
  for i in range(1, n):
    if arr[i] < min_val:
      min_val = arr[i]
    if arr[i] > max_val:
      max_val = arr[i]
  return min_val, max_val

def best_min_max(arr):
  n = len(arr)
  min_val = arr[0]
  for i in range(1, n):
    if arr[i] < min_val:
      min_val = arr[i]

  for i in range(1, n):
    if arr[i] > min_val:
      max_val = arr[i]

  return min_val, max_val

def find_min(arr):
  n = len(arr)
  min_val = arr[0]
  for i in range(1, n):
    if arr[i] < min_val:
      min_val = arr[i]
  return min_val

def find_max(arr):
  n = len(arr)
  max_val = arr[0]
  for i in range(1, n):
    if arr[i] > max_val:
      max_val = arr[i]
  return max_val

def find_min_max_best(arr):
  return find_min(arr), find_max(arr)

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(find_min_max(my_list))
  print(best_min_max(my_list))
  print(find_min_max_best(my_list))