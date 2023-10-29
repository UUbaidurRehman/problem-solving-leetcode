class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,k,r = 0,0,0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l +=1
                r +=1
                k +=1
            elif nums[r] == val:
                r +=1
        return k

