class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        elif n== 3:
            return 2
        num = n
        i = 1
        while i< (n//2)+1: # for i in range(1,n):
            num = num - i
            if num < 0:
                return i-1
            i += 1
        return i-1
        
        
        
        
        
        
        
        
        
        
        
        
        # l,r = 1,n
        # rows = 0
        # while (l<=r):
        #     mid = l+ (r-l)//2

        #     coins = mid/2 * (mid+1)
        #     if coins > n:
        #         r = mid-1
        #     else:
        #         l = mid +1
        #         rows = max(rows, mid)
        # return rows
