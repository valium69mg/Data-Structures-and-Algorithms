
def palindrome_number(number: int) -> bool:  
    num_to_str = str(number)
    if (len(num_to_str) == 1):
        return True
    i = 0
    j = len(num_to_str) - 1    
    while (i<=j):
        print(num_to_str)
        print("Char to analyze at i: " + num_to_str[i])
        print("Char to analyze at j: " + num_to_str[j])
        if (num_to_str[i] == num_to_str[j]):
            print("Chars are equal!")
            if (i == j - 1):
                    return True
            i+=1
            j-=1
        else:
            print("Chars are not equal")
            return False
        if (i == j):
            print("Reach final of the array.")
            return True
        
num = 12321
num2 = 121
num3 = 11

print(palindrome_number(num3))
