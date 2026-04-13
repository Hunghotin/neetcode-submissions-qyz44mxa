class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount+1]*(amount+1)
        cache[0] = 0

        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    cache[i] = min(cache[i], cache[i-c]+1)
        return cache[-1] if cache[-1]<=amount else -1