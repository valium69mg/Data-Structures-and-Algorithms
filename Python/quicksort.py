
def Partition(array,start,end):
    i = start
    j = end - 1
    pivot = array[end]
    while (i < j):
        while i < end and array[i] < pivot:
            i += 1
        while j > start and array[j] >= pivot:
            j -= 1
        if (i<j):
            array[i],array[j] = array[j],array[i] # SWAP
    if array[i] > pivot:
        array[i],array[end] = array[end], array[i]
    return i 

def Quicksort(array,start,end):
    if start < end:
        partition_pos = Partition(array,start,end)
        Quicksort(array,start,partition_pos - 1)
        Quicksort(array, partition_pos + 1, end)


array = [1,5,2,3,9,4,2,9,4,7,3,7,1,9,4,2]
print(array)
array2 = [1,1,2,3,9,4,2,9,4,7,3,7,5,9,4,2]
Quicksort(array,0,len(array)-1)
print(array)
