class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>0:
            res = x
            count = 1
            while True:
                if n>=2*count:
                    res = res*res
                    count *= 2
                    continue
                if n>count:
                    res*=x
                    count+=1
                if count==n:
                    return res
        elif n<0:
            res = 1/x
            count = -1
            while True:
                if n<=2*count:
                    res = res*res
                    count *= 2
                    continue
                if n<count:
                    res = res/x
                    count-=1
                if count==n:
                    return res
        else:
            return 1