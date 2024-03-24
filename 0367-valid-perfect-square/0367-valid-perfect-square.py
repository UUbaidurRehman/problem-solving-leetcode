class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        l = 1
        r = num
        while (l<=r):
            mid = l + (r-l)//2
            if mid == num/mid :# and num%mid==0:
                return True
            elif num > mid*mid :
                l = mid +1
            else:
                r = mid-1
        return False