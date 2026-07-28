class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ndct = {}
        for i in s:
            if i in ndct:
                ndct[i] += 1
            else:
                ndct[i] = 1
        for j in t:
            if j in ndct:
                ndct[j] -= 1
            else:
                return False
        for v in ndct.values():
            if v!=0:
                return False
        print(ndct.values())
        return True
