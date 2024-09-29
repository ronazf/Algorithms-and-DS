class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap = {}
        tmap = {}
        l, r = 0, 0
        curOut = ""
        res = ""
        matches = 0

        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        
        for r in range(len(s)):
            if curOut == "" and s[r] not in tmap:
                l += 1
                continue
            
            curOut += s[r]
            
            if s[r] in tmap:
                smap[s[r]] = smap.get(s[r], 0) + 1
                if smap[s[r]] == tmap[s[r]]:
                    matches += 1

            if matches == len(tmap):
                if res == "":
                    res = curOut
                else:
                    if len(curOut) < len(res):
                        res = curOut
                
                while matches == len(tmap):
                    if l == r:
                        break

                    if s[l] in tmap:
                        if smap[s[l]] == tmap[s[l]]:
                            matches -= 1
                        smap[s[l]] -= 1
                    l += 1
                    if (r - l + 1) < len(res) and matches == len(tmap):
                        res = s[l:r + 1]
                
        return res