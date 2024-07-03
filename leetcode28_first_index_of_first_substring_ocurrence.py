
def strStr(haystack: str, needle: str) -> int:
    i = 0
    j = len(needle) - 1
    if (haystack == needle):
            return 0
    if (needle == ""):
        return -1
    while (i < len(haystack)):
        if (i == len(haystack)):
            return -1
        print("Current window: ")
        print(haystack[i:j+1])
        if (haystack[i:j+1] == needle):
            return i
        i += 1
        j += 1
    return -1 

haystack = "sadbutsad"
needle = "sad"

haystack ="abc"
needle = "c"
print(strStr(haystack,needle))