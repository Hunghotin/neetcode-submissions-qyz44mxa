class Solution:
    def isHappy(self, n: int) -> bool:
        cache = []
        while True:
            if n in cache:
                return False
            cache.append(n)
            tmp = 0
            while True:
                a, b = n//10, n%10
                tmp+=b**2
                print(a, n, tmp)
                n = a
                if n == 0:
                    n = tmp
                    print(n)
                    break
            if n == 1:
                return True