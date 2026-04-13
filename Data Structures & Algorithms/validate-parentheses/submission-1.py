class Solution:
    def isValid(self, s: str) -> bool:
        mem = []
        dct = {'(':')', '{':'}', '[':']'}
        for i in range(len(s)):
            if s[i] in '([{':
                mem.append(s[i])
            else:
                if len(mem)!=0:
                    c = mem.pop()
                else:
                    return False
                if s[i] != dct[c]:
                    return False
        if mem==[]:
            return True
        else:
            return False