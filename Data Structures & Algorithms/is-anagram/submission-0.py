class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        slist = sorted(slist)
        tlist = sorted(tlist)
        print(slist,tlist)
        if slist==tlist:
            return True
        else:
            return False
        
