# First solution by vamsi

def palindrome(s):
    reverse = "" # len(s)
    for i in range(len(s) - 1, -1, -1): # 0(len(s))  
        reverse += s[i]  # O(len(s))
    if s == reverse:  # O(1)
        return True  # O(1)
    else:
        return False # O(1)


# overall time complexity - O(len(s)) + O(len(s)) + O(1) + O(1) + O(1)

s = ""

# print(palindrome(s))

# i/p space - infinity

# o/p space - True/False

# tc - O(len(s)) // 6
# sc - O(len(s))


# second solution by tahir
s = "madam"

def palindrome(s):
    left = 0   # O(1)
    right = len(s) - 1 # O(1)
    while left < right:    # O(len(s)) // 2 3 
        if s[left] == s[right]: # O(1) 2    
            left += 1 # O(1)
            right -= 1  # O(1)
        else:
            return False
    return True

    # overall time complexity - O(len(s)) // 2 * O(1) + O(1) + O(1)
    # O(len(s)) // 2 - 6 // 2 = 3

print(palindrome(s))

# O(len(s))
# O(1)