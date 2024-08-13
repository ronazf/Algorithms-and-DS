from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        
        for i, strObj in enumerate(strs):
            count = [0] * 26
            for letter in strObj:
                count[ord(letter) - ord("a")] += 1
                    
            hashmap[tuple(count)].append(strs[i])

        return hashmap.values()