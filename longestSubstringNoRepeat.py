class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l, r = 0, 0
        length = 0

        if len(s) <= 1: return len(s)

        for i, char in enumerate(s):
            if char in hashmap and hashmap[char] >= l:
                length = max(r - l, length)
                l = hashmap[char] + 1

            hashmap[char] = i
            r += 1

        length = max(length, r - l)
        
        return length