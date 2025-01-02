def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        # calculate mid
        mid = (left + right) // 2
        # comparing 
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [1,2,2,4,5,6,7]
target = 2
print(binary_search(nums, target))
        
# TC : O(log n)
# SC : O(1)


# I/P space -> infinity
# O/P space -> 0 to len(nums)
nums = [1,2,3,4,5,6,7]

# 7 -> 7 // 2
# 3 -> 3 // 2

8 -> 4 -> 2 -> 1

1/2**4 , 2**2 , 2 ** 1

len(nums)/2**n = 1
len(nums) = 2 ** n
n = log(len(nums))



