# Find the maximum sum of all subarrays of size k in an array.

# nums = [1,2,3,4,5,6]
# k = 2
# max_sum of all subarrays 
# o/p:  [1,2], [2,3], [3,4], [4,5], [5,6]
# o/p: 11

# Generate all the k-size subarrays from the given nums 
# calculate sum of elements in the subarray
# Return the max_sum from those 

def max_sum_subarray(nums, k):
    res = []
    max_sum = float("-inf")
    # generate all the subarrays
    n = len(nums)
    for i in range(0, n - k + 1):
        sub = []
        for j in range(i, i + k):
            sub.append(nums[j])
        res.append(sub.copy())
    # calculate sum of elements in the array

    for arr in res:
        sum = 0
        for num in arr:
            sum += num
        # maximize the sum
        max_sum = max(max_sum, sum)
    return max_sum

nums = [1,2,3,4,5,6]
k = 3
print(max_sum_subarray(nums,k))


