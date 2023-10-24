class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = [char for char in s if char.isalnum()]
        li = ''.join(li)
        li = li.lower()
        
        return li == li[::-1]

