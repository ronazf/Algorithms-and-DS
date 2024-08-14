from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        ident = "#"
        for s in strs:
            count = len(s)
            res += str(count) + ident + s
      
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        strIndex = ""
        index = 0
        while index < len(s):
            while s[index] != "#":
                strIndex += s[index]
                index += 1
            keyLen = int(strIndex) + 1
            res.append(s[index + 1: index + keyLen])
            index += keyLen
            strIndex = ""
      
        return res