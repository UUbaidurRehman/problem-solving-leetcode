class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
        # right = len(x)-1

        # for char in x:
        #     if char == x[right]:
        #         right -=1
        #     else:
        #         return False
        # return True
