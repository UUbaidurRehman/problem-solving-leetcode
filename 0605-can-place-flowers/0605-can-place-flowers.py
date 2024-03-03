class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev, count = 0, 0

        for curr in flowerbed:
            if curr == 1:
                if prev == 1:
                    count -= 1
                prev = 1
                
            else: #curr ==0 
                if prev == 1:
                    prev = 0
                else: #prev ==0
                    count += 1
                    prev = 1

        return count >= n