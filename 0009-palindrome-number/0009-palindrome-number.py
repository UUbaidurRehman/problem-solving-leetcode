class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        right = len(x)-1
        for char in x:
            if char == x[right]:
                right -=1
            else:
                return False
        return True
