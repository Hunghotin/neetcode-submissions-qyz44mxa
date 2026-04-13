import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sys.setrecursionlimit(100000)
        cache = {}
        def dfs(amount):
            if amount in cache:
                return cache[amount]
            if amount==0:
                cache[amount]=0
                return 0

            res = 1e9
            for c in coins:
                if amount-c>=0:
                    res = min(res, 1+dfs(amount-c))
            cache[amount] = res
            return res
        for i in range(amount+1):
            res = dfs(amount)
        return -1 if res==1e9 else res