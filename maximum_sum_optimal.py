# nums = [1,2,3,4,5,6]


# iterate through possible indices
# sum of the window
# max_sum and store max_sum

def optimal_max_sum(nums, k):
    n = len(nums)
    max_sum = float("-inf")
    current_sum = 0
    left = 0
    print("current_sum: ", current_sum)
    # I am just getting the first window size [10,2,40,5,70,20,35] k = 2 current_sum = 3
    # n = 6 k = 3, 3 -> 5
    for i in range(0, k):
        current_sum += nums[i]
    print("current_sum: ", current_sum)
    for right in range(k, n):
        current_sum = current_sum + nums[right] - nums[left]
        print("window_sum: ", current_sum)
        max_sum = max(max_sum, current_sum)
        left += 1
    return max_sum


nums =  [10,2,40,5,70,20,35]
k = 3
print(optimal_max_sum(nums, k))



