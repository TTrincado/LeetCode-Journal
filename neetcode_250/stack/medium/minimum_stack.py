class MinStack:
    """
    First approach, fails in the condition of having all of the operations run in O(1) time.

    Time Complexity:
      - push, pop, top: O(1)
      - getMin: O(N). We have to traverse the whole stack to find the minimum, 
        then put everything back.
    Space Complexity: O(N).
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while self.stack:
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while tmp:
            self.stack.append(tmp.pop())

        return mini

class MinStack2:
    """
    Approach: Two Stacks.
    
    Logic:
    We maintain a secondary stack ('minStack') that mirrors the main stack ('stack')
    and that keeps track of the current minimum value found in the main stack.
    
    Time Complexity: O(1) for all operations.
    Space Complexity: O(N) (Two stacks store N elements each).
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If minStack has elements, check if the new value being pushed
        # is a smaller value than the current ones stored
        if self.minStack:
            val = min(val, self.minStack[-1])
        
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() # Pop to roll back the minimum state before that value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]