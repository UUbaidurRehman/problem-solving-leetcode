class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0:
                if i ==0 or flowerbed[i-1] == 0: 
                    prev = True
                else: 
                    prev = False
                if i == size-1 or flowerbed[i+1] == 0: 
                    nextt = True 
                else: 
                    nextt = False
                if prev and nextt:
                    count += 1
                    flowerbed[i] = 1
            if count >= n: return True
        return False


