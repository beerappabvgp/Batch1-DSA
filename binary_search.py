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
        
