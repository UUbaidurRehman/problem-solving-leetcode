class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <=1:
            return n
        i = 1
        j = n
        while (i <= j):
            if n >= i:
                n -= i
                
            else:
                return i-1
            i += 1