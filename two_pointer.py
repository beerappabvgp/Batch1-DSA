class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        reader = 0
        writer = 0

        for n in nums:
            if n == val:
                reader += 1
            elif n != val:
                nums[writer] = n
                reader += 1
                writer += 1
        return writer
            



        # # I/p:  [1,2,3,4,5,2,2] val = 2




            #     [1,2,3,4,5,2,2]


            
        # len(nums) = 7
        # # o/p : [1,3,4,5] , res = 4
        # 1. [1,3,4,5] -> len(res)


        #  [1,2,3,4,5,2,2]

        #  res = [1,3,4,5,5,2,2]
        # reader = 0
        # writer = 0
        # # 2
        # reader = 1
        # writer = 1
        # # 3
        # reader = 2
        # writer = 1
        # # 4
        # reader = 3
        # writer = 2
        # # 5
        # reader = 4
        # writer = 3
        # # 6
        # reader = 5
        # writer = 4
        # #  7
        # reader = 6
        # writer = 4

        
