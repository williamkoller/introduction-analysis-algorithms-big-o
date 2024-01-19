def find_max(numbers):
  max_number = numbers[0]
  for number in numbers:
    if number > max_number:
      max_number = number
  return max_number

if __name__ == "__main__":
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(find_max(numbers))
