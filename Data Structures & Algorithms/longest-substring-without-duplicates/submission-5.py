class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cache = []
        l = 0
        res = 0

        for r in range(n):
            while s[r] in cache:
                cache.pop(0)
                l+=1
            cache.append(s[r])
            res = max(res, r-l+1)
        return res