from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        length = len(temps)
        stack = []
        res = [0] * length

        for i in range(length):
            while stack and temps[stack[-1]] < temps[i]:
                index = stack.pop()
                res[index] = i - index
            
            stack.append(i)
        return res