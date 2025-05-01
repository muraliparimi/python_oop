class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        # print(f"after pushing {val} the stack is {self.stack}")
        # print(f"after pushing {val} the min_stack is {self.min_stack}")

    def pop(self) -> None:
        if self.top() == self.min_stack[-1]:
            # print("top and min are mathing, so we need to remove them both")
            self.stack.pop()
            self.min_stack.pop()
        else:
            self.stack.pop()
        # print(f"after popping the stack is {self.stack}")
        # print(f"after popping the min_stack is {self.min_stack}")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(-2)
    minStack.push(-3)
    minStack.push(-3)
    # minStack.push(0)
    print(minStack.getMin()) # // return 0
    minStack.pop()
    # minStack.top()    # // return 2
    print(minStack.getMin()) # // return 1