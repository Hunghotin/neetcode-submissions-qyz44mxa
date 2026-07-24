class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0]*26

        for c in s:
            record[ord(c)-ord('a')]+=1
        
        for j in t:
            record[ord(j)-ord('a')]-=1
        
        if record==[0]*26:
            return True
        else:
            return False