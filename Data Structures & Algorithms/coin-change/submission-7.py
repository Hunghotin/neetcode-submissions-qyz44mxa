class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:#每轮循环看应该取哪一枚硬币
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # 是否取一个面值为c的硬币
        return dp[amount] if dp[amount] != amount + 1 else -1