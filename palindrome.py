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

print(palindrome(s))

# i/p space - infinity

# o/p space - True/False

# tc - O(len(s))
# sc - O(len(s))

