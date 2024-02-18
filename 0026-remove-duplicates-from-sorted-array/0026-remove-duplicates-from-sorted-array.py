class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # r = 0
        # l = 0
        # while r < len(nums):
        #     if nums[l] != nums[r]:
        #         l = l + 1
        #         nums[l] = nums[r]
        #     r = r + 1
        # return l+1

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l = l + 1
        return l
            

