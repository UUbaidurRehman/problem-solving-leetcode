class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r,l = len(nums)-1,0
        while l< r:
            mid = l+ (r-l)//2
            if target > nums[mid]:
                l = mid+1
            else: #target < nums[mid]:
                r = mid
        if (nums[l] == target): 
            return l
        else:
            return -1