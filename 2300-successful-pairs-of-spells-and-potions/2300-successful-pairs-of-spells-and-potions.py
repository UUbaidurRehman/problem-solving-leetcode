class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        count_pair = []
        len_p = len(potions)-1
        for i in spells:
            count = 0
            l,r = 0, len_p
            while l <= r:
                mid = l + (r-l)//2
                product = i*potions[mid]
                if  product < success:
                    l = mid+1
                elif product >= success:
                    r = mid-1
            count = len_p - r
            count_pair.append(count)
        return count_pair