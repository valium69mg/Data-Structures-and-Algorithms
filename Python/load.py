file_name = "D:/My files/Python OOP/data structure and algorithms/Python/numbers.txt"
def load_numbers(file_name):
  numbers = []
  with open(file_name) as f:
    for line in f:
      numbers.append(int(line))
  return numbers


numbers = load_numbers(file_name)

