class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        minVal = val
        if self.arr:
             minVal = min(minVal, self.arr[-1][1])
        self.arr.append([val, minVal])

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        return -1 if not self.arr else self.arr[-1][0]

    def getMin(self) -> int:
        return -1 if not self.arr else self.arr[-1][1]
