class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a= []
        for n in range(1 , n+1):
            if n % 3 == 0 and n % 5 == 0 :
                a.append("FizzBuzz")
            elif n % 3 == 0 :
                a.append("Fizz")
            elif n % 5 == 0 :
                a.append("Buzz")
            else:
                 a.append(str(n))
            
        return a