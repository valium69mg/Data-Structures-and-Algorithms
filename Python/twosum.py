
# CHECK FOR NEGATIVE NUMBERS
def twoSum(nums, target):
    i = 0
    hash_table = {}
    while (i < len(nums)):

        if (target - nums[i] in hash_table):
            firstIndex = hash_table[target - nums[i]]
            return [firstIndex,i]
        else:
            hash_table[nums[i]] = i
        if i >= len(nums):
            return []
        i+=1

        

array = [-10,7,19,15]
target = 9

array2 = [3,5,2,7]
target2 = 9

array3 = [3,3]
target3 = 6

array4 = [3,2,4]
target4 = 6

print(twoSum(array2,target2))