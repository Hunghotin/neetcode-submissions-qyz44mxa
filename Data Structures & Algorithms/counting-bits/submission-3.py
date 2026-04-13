class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        max_i = 0
        for i in range(n+1):
            if i//2**(max_i+1)==1:
                max_i += 1
            tmp = 0
            j = max_i
            while i>0:
                if i//2**j==1:
                    tmp+=1
                    i-=2**j
                j-=1
            res.append(tmp)
        return res