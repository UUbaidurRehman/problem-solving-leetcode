class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if (s == s[::-1]):
        #     return True
        right = len(s)-1

        for left in range(len(s)):
            if s[left] != s[right]:
                string1 = s[:left]+ s[left+1:]
                string2 = s[:right] + s[right+1:]
                return string1 ==string1[::-1] or string2 ==string2[::-1]
            right -=1
        return True
