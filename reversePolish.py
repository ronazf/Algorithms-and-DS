from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = { "+", "-", "*", "/" }

        for token in tokens:
            if token not in operations:
                stack.append(token)
                continue
            
            first = int(stack[-2])
            second = int(stack[-1])
            res = 0
            match token:
                case "+":
                    res = first + second
                case "-":
                    res = first - second
                case "*":
                    res = first * second
                case "/":
                    res = int(first / second)
            stack.pop()
            stack.pop()
            stack.append(str(res))
        
        return int(stack[-1])