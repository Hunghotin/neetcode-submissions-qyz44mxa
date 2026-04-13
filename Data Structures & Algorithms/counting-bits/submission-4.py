class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        max_i = 1
        for i in range(1,n+1):
            if i == max_i*2:
                max_i = i
            res[i] = res[i-max_i]+1
        return res