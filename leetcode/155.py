# 155. Min Stack

# Approach 1. Time complexity is bad
# Time Complexity: O(n^2)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0: 
            return -1 
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

# Approach 2.
# Time Complexity: O(n)
class MinStack:

    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    # @return nothing
    def pop(self):
        self.stack.pop()


    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][0]


    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][1]
        