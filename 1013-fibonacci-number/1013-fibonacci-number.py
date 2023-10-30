class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        elif n==0:
            return 0
        fib_num = (self.fib(n-1)+self.fib(n-2))
        return fib_num