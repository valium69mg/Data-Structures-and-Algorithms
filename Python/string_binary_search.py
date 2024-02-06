from string_quick_sort import sorted_names

def binary_search(collection,target):
    first = 0
    last = len(collection) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


searched_string_index = binary_search(sorted_names,"Mikey Vaughan")
