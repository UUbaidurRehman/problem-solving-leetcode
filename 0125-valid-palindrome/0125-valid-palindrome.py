class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for char in s:
            if char.isalnum() == True:
                ss += char
        ss = ss.lower()
        print(ss)
        return ss == ss[::-1]
