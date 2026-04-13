class Solution:
    def isHappy(self, n: int) -> bool:
        cache = []
        while True:
            if n in cache:
                return False
            cache.append(n)
            tmp = 0
            n_str = str(n)
            for s in n_str:
                tmp+=int(s)**2
            n=tmp
            if n == 1:
                return True