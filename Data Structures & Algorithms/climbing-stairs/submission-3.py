class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def dfs(i):
            if i==1:
                return 1
            elif i==2:
                return 2


            if i in memo:
                return memo[i]
            else:
                memo[i]=dfs(i-1)+ dfs(i-2)

            return memo[i]

        return dfs(n)