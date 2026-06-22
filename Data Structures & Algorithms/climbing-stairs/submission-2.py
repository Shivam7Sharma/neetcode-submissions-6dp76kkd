class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def recur(n):
            if n==1:
                return 1
            elif n==2:
                return 2
            
            if n in memo: return memo[n]
            else:
                memo[n]= recur(n-1)+recur(n-2)

            return memo[n]

        return recur(n)
