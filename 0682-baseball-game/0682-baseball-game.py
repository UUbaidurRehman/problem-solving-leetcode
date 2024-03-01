class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == "+":
                # if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        for i in stack :
            total += i
        return total
