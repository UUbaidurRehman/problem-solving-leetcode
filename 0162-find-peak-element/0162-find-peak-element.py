class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        l,r= 0, len(nums)-1
        while l < r:
            mid =  l + (r-l)//2
            
            if nums[mid+1] > nums[mid]:
                l = mid + 1
            else: #nums[mid-1] < nums[mid]
                r = mid
        return l