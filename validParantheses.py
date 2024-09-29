class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False

        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
                continue
            
            if stack == []:
                return False
            
            if (c == ']' and stack[-1] != '[') or (c == ')' and stack[-1] != '(') or (c == '}' and stack[-1] != '{'):
                return False
            
            stack.pop()
        
        if stack == []:
            return True
        
        return False