class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = [0] * 26
        l, r = 0, 0
        flip = 0
        maxRpt = 0
        res = 0
        while r < len(s):
            index = ord(s[r]) - ord("A")
            alphabet[index] += 1
            maxRpt = max(maxRpt, alphabet[index])

            if r - l + 1 - maxRpt <= k:
                res = max(res, r - l + 1)
                r += 1
                continue
            
            index = ord(s[l]) - ord("A")
            alphabet[index] -= 1
            l += 1
            r += 1

        return res