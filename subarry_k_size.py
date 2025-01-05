# def k_size_subarray(nums, k):
#     # for sure each subarray will start from every single index present in the nums array 
#     n = len(nums)
#     res = []  # O(n - k + 1)
#     for i in range(0, n - k + 1):  # 0(n-k+1)
#         subarray = []  # O(k)
#         # traverse the next k elements to get the k size subarray 
#         for j in range(i, i+k):  # O(k)

#         # adding the subarray to the res
#         res.append(subarray.copy())
#     return res  


def optimal_size_k(nums, k):
    res = []
    # iterate every index
    n = len(nums)
    sub = []  # reference to the memory location 
    left = 0
    # nums = [1,2,3,4]
    # n = 4, k = 2 => 0 -> 3
    # python ranges are exclusive 0 -> 3 => 0,1,2 
    # 0 -> 4 => [0,1,2,3]
    for i in range(0, n - k + 2):  # O(n - k + 2)
        # whenever you are updating with new values the address location will never change 
        sub.append(nums[i])
        if len(sub) > k:
            sub.pop(0)
        if len(sub) == k:
            res.append(sub.copy())
    return res

# Tc = O(n - k + 2) 
# SC : O(n - k + 1) * O(k)


nums = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("please enter the size of window : "))
# print(k_size_subarray(nums, k))
print(optimal_size_k(nums, k))

# nums = [1,2,3,4,5] k = 3 n = 5
# nums = [1,2,3,4] k = 2, n = 4
# [1,2,3,4] => n - k = 2 + 1
# I/p Space => infinity
# O/p Space => n - k + 1 => 5 - 3 + 1 = 3

# ArrayList<Integer> nums = new ArrayList<Integer>();
# nums.add(1);

# nums = [1,2,3,4,5]
# k-size subarray from the above array 

# k = 2
# subarray => subset of array , continuous
# [1,2]
# [2,3]
# [3,4]
# [4,5]


# approach 1: nums = [1,2,3,4] k = 2, n = 4
# TC: O(n - k + 1) * O(k) => 6
# SC: O(n - k + 1) * O(k)







# nums  = [1,2,3,4], n = 4, k = 2
# o/p space = n - k + 1 = 4 - 2 + 1 = 3


#  n = len(nums)
    # res = []  # O(n - k + 1)
    # for i in range(0, n - k + 1):  0 to 3 => 3 operations
        # subarray = []      O(1) => 1 operation
    #     # traverse the next k elements to get the k size subarray 
    #  i = 1
    #  k = 2
    #     for j in range(i, i+k):  i -> i + k => 1 -> 1 + 2 => 1 - 3 => 2 operations => k operations

    #     # adding the subarray to the res
    #     res.append(subarray.copy())
    # return res  


# 3 + 2 => 5 operations
# 3 * 2 => 6 operations 
# for each iteration two operations will occur 
# 1 -> 2
# 2 -> 2
# 3 -> 2
# 6 
# for i in range(n):
    # for j in range(n):
    #    for k in

# Tc: O(n**3)