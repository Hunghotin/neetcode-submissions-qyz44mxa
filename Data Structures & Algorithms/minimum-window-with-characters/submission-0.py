class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdct = {}
        for c in t:
            tdct[c] = tdct.get(c, 0)+1
        
        res = ''
        minl = len(s)
        needed = len(tdct)
        for i in range(len(s)):
            sdct = {}
            cur = 0
            for j in range(i, len(s)):
                sdct[s[j]]=sdct.get(s[j],0)+1
                if s[j] in tdct and sdct[s[j]]==tdct[s[j]]:
                    cur+=1
                if cur == needed:
                    if minl >= j-i+1:
                        minl = j-i+1
                        res = s[i:j+1]
        return res

                    

            


            
