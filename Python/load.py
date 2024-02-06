file_name = "D:/My files/Python OOP/data structure and algorithms/Python/numbers.txt"
file_name_strings = "D:/My files/Python OOP/data structure and algorithms/Python/names.txt"
def load_numbers(file_name):
  numbers = []
  with open(file_name) as f:
    for line in f:
      numbers.append(int(line))
  return numbers

def load_names(file_name_strings):
  strings = []
  with open(file_name_strings) as f:
    for line in f:
      strings.append(line.rstrip('\n'))
  return strings


numbers = load_numbers(file_name)
strings = load_names(file_name_strings)

