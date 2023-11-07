class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=5:
            if x==0:
                return 0
            elif x<4:
                return 1
            else:
                return 2
        l , r = 0,x//2
        res = 0
        while (l<r):
            mid = l+ (r-l)//2
            if mid*mid < x:
                l= mid+1
                res = mid
            elif mid* mid > x:
                r = mid
            else:
                return mid
                
        return res
        
                
        
       
