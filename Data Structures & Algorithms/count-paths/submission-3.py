class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        previrow=[1]*n

        for i in range(m-1):
            currrow=[1]*n

            for j in range(n-2,-1,-1):
                currrow[j]=currrow[j+1]+previrow[j]

            previrow=currrow

        return previrow[0]