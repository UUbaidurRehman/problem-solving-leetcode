class Solution:
    def mySqrt(self, x: int) -> int:
        l , r = 0,x
        if x==0:
            return 0
        elif x < 4:
            return 1
        elif r*r ==x:
            return r
        while (l<r):
            mid = l+ (r-l)//2
            if mid*mid == x:
                return mid
            elif mid* mid > x:
                r = mid
            else:
                l= mid+1
                res = mid
        return res
        
                
        
       
