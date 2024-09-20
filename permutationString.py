class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        s2map = {}
        l = 0
        matches = 0

        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1
        
        mapLen = len(s1map)
        
        for r in range(len(s2)):
            if s2[r] not in s1map:
                s2map = {}
                matches = 0
                l = r + 1
                continue
            
            s2map[s2[r]] = s2map.get(s2[r], 0) + 1

            if s2map[s2[r]] == s1map[s2[r]]:
                matches += 1

            while s2map[s2[r]] > s1map[s2[r]]:
                if s2map[s2[l]] == s1map[s2[l]]:
                    matches -= 1
                s2map[s2[l]] -= 1
                l += 1

            if matches == mapLen:
                return True
        
        return False