"""
Title: linear search 
Author: carlostr
Date: 01/02/2024
"""

numbers = [1,2,3,4,5,6,7,8,9,10]

def linear_search(list,target):
    """
    Returns the index position of the target if found, else returns None
    """
    len_of_list = len(list)
    for i in range(0,len_of_list):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found !!!")


