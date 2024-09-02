class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        beg = 0
        end = len(s) - 1

        while beg < end:
            if not self.alphaNum(s[beg]):
                beg += 1
                continue
            if not self.alphaNum(s[end]):
                end -= 1
                continue
            if s[beg] != s[end]:
                return False
            beg += 1
            end -= 1
        
        return True
    
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))