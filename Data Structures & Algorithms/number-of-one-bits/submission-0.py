class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(31,-1,-1):
            if n//2**i==1:
                res+=1
                n -= 2**i
        return res