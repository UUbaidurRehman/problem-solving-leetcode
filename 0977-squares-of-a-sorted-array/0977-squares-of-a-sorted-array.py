class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sqred = [0]*n
        l,r = 0,n-1
        while l<= r:
            left, right = abs(nums[l]),abs(nums[r])
            if left < right:
                sqred[r-l] = right*right
                r -= 1
            else:
                sqred[r-l] = left*left
                l += 1
        return sqred
