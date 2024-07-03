# BINARY SEARCH IN PYTHON
def binarySearch(array,target):
    p1,p2 = 0,len(array) - 1
    while p1 <= p2:
        mid = p1 + (p2-p1)//2 # 
        
        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            p2 = mid - 1
        else:
            p1 = mid + 1
    # IF NOT FOUND WE SEARCH FOR BOTH SIDES ADJACENT TO THE POINTERS (P1 = P2)
    if (p1 == len(array) - 1): # AT THE END WE ONLY CHECK FOR LEFT ELEMENT
        if (array[p1] < target):
            return len(array) # RETURN THE END + 1 RIGHT INDEX POS
        else:
            return p1 # RETURN THE LEFT INDEX POSITION
    elif(p1 <= 0): # AT THE BEGENNING WE ONLY CHECK FOR RIGHT INDEX POSITION
        if (array[p1] > target):
            return 0
        else:
            return p1
    else:
        # IF P1 STAYED OUT OF BOUNDS
        if (p1 >= len(array)):
            return p1
        # OTHER CASES WHERE THERE ARE BOTH ADJACENT NUMBERS OF POINTER
        if (array[p1] > target): #RIGHT INDEX
            return p1
        else:
            return p1 + 1 

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
array2 = [1,3,5,6]
print(binarySearch(array2,7))

