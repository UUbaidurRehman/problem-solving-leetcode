class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []        

    def push(self, val: int) -> None:
        if len(self.minstack) == 0 or val <= self.minstack[-1] :
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if self.minstack[-1] == pop:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1] 
        # return self.stack[len(stack)-1]

    def getMin(self) -> int:
        return self.minstack[-1]

    
    
    # def top(self) :
    #     return self.stack[len(self.stack)-1]
    # def getMin(self) -> int:
    #     return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()