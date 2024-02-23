class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            window = s[i:i+3]
            isDistinct = True
            seen = set()
            for char in window:
                if char in seen:
                    isDistinct = False
                    break
                seen.add(char)
            if isDistinct:
                count +=1
        return count