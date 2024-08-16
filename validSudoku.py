from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty = "."
        for i in range(9):
            hashSet = set()
            for j in range(9):
                if board[i][j] != empty and board[i][j] in hashSet:
                    return False
                else:
                    hashSet.add(board[i][j])
      
        for i in range(9):
            hashSet = set()
            for j in range(9):
                if board[j][i] != empty and board[j][i] in hashSet:
                    return False
                else:
                    hashSet.add(board[j][i])

        for i in range(3):
            for j in range(3):
                hashSet = set()
                for k in range(9):
                    curVal = board[i * 3 + int(k / 3)][j * 3 + k % 3]
                    if curVal != empty and curVal in hashSet:
                        return False
                    else:
                        hashSet.add(curVal)
      
        return True