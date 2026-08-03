class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:  
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        tmp = []
        mini = self.top()
        while self.stack:
            head = self.pop()
            tmp.append(head)
            mini = min(mini, head)
        
        while tmp:
            self.push(tmp.pop())
        
        return mini