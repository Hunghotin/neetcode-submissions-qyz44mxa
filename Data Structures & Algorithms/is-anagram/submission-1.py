class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdct = {}
        tdct = {}
        for c in s:
            sdct[c] = sdct.get(c,0)+1
        for c in t:
            tdct[c] = tdct.get(c,0)+1
        if sdct == tdct:
            return True
        else:
            return False
        
