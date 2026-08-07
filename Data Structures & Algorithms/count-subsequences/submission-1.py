class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*(len(t)+1) for i in range(len(s)+1)]
        def finder(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            a = s[i]
            b = t[j]
            res = finder(i+1,j)
            if a == b:
                res += finder(i+1,j+1)
            if dp[i][j]==-1:
                dp[i][j] = res
            return res
        
        return finder(0,0)
