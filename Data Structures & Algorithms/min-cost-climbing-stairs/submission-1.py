class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo=[-1]*len(cost)

        def mincost(i):
            if i>=len(cost):
                return 0
            
            if memo[i]!=-1:
                return memo[i]

            memo[i]= cost[i]+ min(mincost(i+1), mincost(i+2))

            return memo[i]

        return min(mincost(0), mincost(1))