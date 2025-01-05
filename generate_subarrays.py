# Given an input array you need to generate all the possible outputs that is part of array 

# generate all the subarrays 

def generate_subarrays(nums):
    # I wanted to start with each and every index in the array right
    n = len(nums)
    # 0 -> n
    res = []
    for i in range(n): 
        # [1,2,3,4]
        print("================================")
        subarray = []
        for j in range(i, n):
            subarray.append(nums[j])
            print("Before appending ... ")
            # [1,2,3]
            # subarray.copy() => [1,2,3]
            res.append(subarray.copy())
            print(res)
            print("after appending ... ")
            print("===========completed================")

    return res
            
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(generate_subarrays(nums))






# i/p space :  Infinity
# O/p space: depends on input 
# let us say n = len(nums)
# then the o/p space is n(n+1)/2


# call by value and call by reference  

# nums = [1,2]
# res = [[1, 2]]
# nums = 0xassdf
# num = 10
# num = 0xasdd



#   for i in range(n): 
#         # [1,2,3,4]
#         subarray = []
#         for j in range(i, n):
#             subarray.append(nums[j])
#             res.append(subarray)

#     return res