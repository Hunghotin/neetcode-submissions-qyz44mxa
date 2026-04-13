class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        res = 0
        for i in range(len(s)-1):
            count = 1
            for j in range(i+1, len(s)):
                print(count, s[j], s[i:j])
                if s[j] not in s[i:j]:
                    count+=1
                else:
                    break
            res = max(count, res)
        return res