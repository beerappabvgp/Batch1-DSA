def k_size_subarray(nums, k):
    # for sure each subarray will start from every single index present in the nums array 
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        subarray = []
        # traverse the next k elements to get the k size subarray 
        for j in range(i, i+k):
            subarray.append(nums[j])
        # adding the subarray to the res
        res.append(subarray.copy())
    return res  

nums = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("please enter the size of window : "))
print(k_size_subarray(nums, k))

# nums = [1,2,3,4,5] k = 3 n = 5
# nums = [1,2,3,4] k = 2, n = 4
# I/p Space => infinity
# O/p Space => n - k + 1 => 5 - 3 + 1 = 3