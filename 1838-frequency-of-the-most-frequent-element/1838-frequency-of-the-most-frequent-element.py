class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            if  nums[r]*(r-l+1) > total + k:
                total -= nums[l]
                l +=1
            res = r-l+1
            r +=1
        return res