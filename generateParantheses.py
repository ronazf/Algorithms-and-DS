from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(self, openVal: int, closeVal: int, total: str):
            openVal = openVal
            closeVal = closeVal
            total = total

            if openVal < n:
                if closeVal < openVal:
                    backTrack(self, openVal, closeVal + 1, total + ")")
                
                backTrack(self, openVal + 1, closeVal, total + "(")
            else:
                while closeVal < openVal:
                    total += ")"
                    closeVal += 1
                res.append(total)
        
        backTrack(self, 0, 0, "")
        
        return res