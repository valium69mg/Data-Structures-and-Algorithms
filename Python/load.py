file_name = "D:/My files/Python OOP/data structure and algorithms/Python/numbers.txt"
file_name_strings = "D:/My files/Python OOP/data structure and algorithms/Python/unsorted_names.txt"
def load_numbers():
  numbers = []
  with open(file_name) as f:
    for line in f:
      numbers.append(int(line))
  return numbers

def load_names():
  strings = []
  with open(file_name_strings) as f:
    for line in f:
      strings.append(line.rstrip('\n'))
  return strings


numbers = load_numbers()
strings = load_names()



