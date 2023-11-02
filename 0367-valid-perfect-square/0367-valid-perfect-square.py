class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l,r= 1,num//2
        while (l <= r):
            mid = l + (r-l)//2
            if mid*mid > num:
                r = mid -1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False