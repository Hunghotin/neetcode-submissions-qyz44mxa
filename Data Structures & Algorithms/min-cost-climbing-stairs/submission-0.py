class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [0]*n
        if n==1:
            return cost[0]
        if n==2:
            return min(cost[0],cost[1])

        min_cost[-1] = cost[-1]
        min_cost[-2] = cost[-2]
        for i in range(n-3, -1, -1):
            min_cost[i] = min(min_cost[i+1], min_cost[i+2])+cost[i]

        return min(min_cost[0],min_cost[1])
            
