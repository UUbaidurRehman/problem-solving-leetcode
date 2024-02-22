class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r= 0,1
        while r<len(nums):
            if nums[l] == 0: 
                if nums[r] != 0 :
                    nums[l], nums[r] = nums[r],nums[l]
                    l +=1
            else: l += 1
            r +=1

        # snowball = 0 
        # for i in range (len(nums)):
        #     if nums[i] == 0 :
        #         snowball +=1
        #     elif snowball > 0:
        #         t = nums[i]
        #         nums[i] = 0 
        #         nums[i-snowball] = t
        