class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS, hashmapT = {}, {}

        # different lengths
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1
      
        return hashmapS == hashmapT