
def merge_sort(list):
    """
    Sorts a list in ascending order 

    divide: find the midpoint of the list and ficide into sublists
    conquer: recursively sort the sublists created in previos step
    combine: merge the sorted sublists created in previous steps

    Runs in O(k*n log n) time
    """

    if len(list) <= 1:
        return list
    left_half,right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)
    
def split(list):
    """
    Divide the unsorted list at midpoint into sublists 
    Return two sublists - left and right 

    Runs in overall O(k log n) time (logarithmic time)
    """
    #Slice function in python runs in O(K)
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left,right

def merge(left,right):
    """
    This function merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time (linear time)
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    """
    Verifies that a list is sorted using a recursive method
    """
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:]) #Recursive call




alist = [54,62,93,17,77,31,44,55,20]
l = merge_sort(alist)
print(l)
print(verify_sorted(l))