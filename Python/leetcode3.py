# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS


def lengthOfLongestSubstring(s: str) -> int:
    dict = {}
    i = 0
    j = 1
    longestSubstring = 0
    if (len(s) == 1):
            return 1
    elif (len(s) <= 0):
        return 0
    while (i < len(s) - 1):
        dict[s[i]] = i # APPEND VALUE OF I AND INDEX 
        print("Interation: ")
        print("Adding value of i to dict")
        print(dict)
        print("i: " + str(i))
        print("j: " + str(j))
        
        if (len(dict) > longestSubstring): 
            longestSubstring = len(dict)
        
        if (i >= len(s) - 1):
            break
        if (j>= len(s)):
            break


        if (s[j] not in dict):
            print("Letter: " + s[j] + " not in hashmap")
            dict[s[j]] = j
            j+=1
            print("Curent max substring: " + str(longestSubstring))

        else:
            dict = {} # EMPTY THE DICT
            i+=1
            j = i + 1

    return longestSubstring
# USING A SET
def length_of_longest_substring(s: str) -> int:
    my_set = set()
    i = 0
    j = 1
    longestSubstring = 0
    if (len(s) == 1):
            return 1
    elif (len(s) <= 0):
        return 0
    while (i < len(s) - 1):
        my_set.add(s[i]) # APPEND VALUE OF I AND INDEX 
        print("Interation: ")
        print("Adding value of i to dict")
        print(my_set)
        print("i: " + str(i))
        print("j: " + str(j))
        if (len(my_set) > longestSubstring): 
            longestSubstring = len(my_set)     
        if (i >= len(s) - 1):
            break
        if (j>= len(s)):
            break
        if (s[j] not in my_set):
            print("Letter: " + s[j] + " not in hashmap")
            my_set.add(s[j])
            j+=1
            print("Curent max substring: " + str(longestSubstring))

        else:
            my_set.clear() # EMPTY THE DICT
            i+=1
            j = i + 1
    return longestSubstring

input = "abcabcbb"
print(length_of_longest_substring(input))
#print(length_of_longest_substring("au"))