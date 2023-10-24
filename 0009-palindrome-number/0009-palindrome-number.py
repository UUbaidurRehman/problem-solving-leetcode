class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        temp = x
        num= 0
        while (temp > 0):
            num = num*10 + (temp % 10)
            temp = temp//10
        return x == num 