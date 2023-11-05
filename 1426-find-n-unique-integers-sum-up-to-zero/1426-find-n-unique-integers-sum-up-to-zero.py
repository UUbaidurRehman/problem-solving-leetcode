import random
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        arr = []
    
        for i in range(1,(n//2)+1):
            arr = [i] + arr +[-i]
            
        if n%2 != 0 :
            arr += [0]
        return arr
