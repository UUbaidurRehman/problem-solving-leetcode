class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l= 0 
        for r in range (len(nums)):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l += 1
        return l+1