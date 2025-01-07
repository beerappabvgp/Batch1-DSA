# This is for testing purposes 

# # [1,2,3,4,5]
# # traversal, adding , removing, searching , sorting , updating , deleting 

# # nums = [1,2,3,4,5]
# # o/p : 1,2,3,4,5
# # nums = [2]
# # nums = [0,45]


# # i/p  -> algorithm -> o/p

# # traversal

# # i/p space and o/p space 
# # i/p space - infinity

# # o/p space - set of values (len of array)

# nums = [1,2,3,4,5]
# n = 5
# 0 -> 4


# 0,1,2,3,4

# left_traversal(nums)
    # 1. n = len(numscall the function 

    # left_traversal(nums)
#     2. iterate from 0 to n - 1
#     3. system.out.println(nums[i])



# nums = [1,2,3,4,5]
# def left_traversal(nums):
#     n = len(nums)
#     for i in range(0, n):
#         print(nums[i])
# # call the function 

# def right_to_left(nums):
#     n = len(nums)
#     # 4 -> 3 -> 2 -> 1 -> 0
#     for i in range(n-1, -1, -1):
#         print(nums[i])
# right_to_left(nums)
# # left_traversal(nums)

# # adding 

# # searching 

# # day 0 

# nums = [1,2,4,5,6,7]

# whether 40 exists in the array or not 

# i/p -> algo -> o/p

# input space -> infinity 

# output space -> 2 t/f

# nums = [1,2,4,5,6,7,40]

# 1. for 0 -> n
#         1 == 40
# 2.  if nums[i] != 40:
#       continue
#     else:
#       return True 

# o/p : False


# def search(nums, target):
#     n = len(nums)
#     for i in range(0, n):
#         if nums[i] != target:
#             print("false")
#             continue
#         else:
#             return True




# Time Complexity and space complexity 

# # TC : O(n)
# # n = len(nums)
# [1,2,4,567,45]  // 5 
# [1,2,3,4,5,56,67,6] // 8 -> target - 1 - O(1)


# def linear_search(nums, target):
#     n = len(nums)
#     for i in range(0, n):
#         if nums[i] == target:
#             return True
#     return False

# O(1) - SC
# print(search([1,2,3], 30))
