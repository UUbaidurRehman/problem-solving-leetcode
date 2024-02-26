class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        size = 0
        window = ''
        for i in range(len(s)):
            if s[i] in window:
                length = max(size, length)
                while s[i] in window:
                    window = window[1:]
            window = window + s[i]
            size = len(window)
        return max(length, size)


