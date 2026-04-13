class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = []
        result = []
        for string in strs:
            sdict = {}
            for c in string:
                sdict[c] = sdict.get(c,0)+1
            if sdict not in cache:
                cache.append(sdict)
                result.append([string])
            else:
                index = cache.index(sdict)
                result[index].append(string)
        return result
