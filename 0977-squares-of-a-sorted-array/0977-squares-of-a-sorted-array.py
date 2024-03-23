class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sqred = [0]* (len(nums))
        sqred = []
        l,r = 0,len(nums)-1
        while l<= r:
            if nums[l]**2 > nums[r]**2:
                sqred.append(nums[l]**2)
                l +=1
            elif nums[l]**2 <= nums[r]**2:
                sqred.append(nums[r]**2)
                r -=1
        return sqred[::-1]
            
