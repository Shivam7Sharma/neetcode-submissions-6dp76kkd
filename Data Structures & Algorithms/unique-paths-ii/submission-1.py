class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS= len(obstacleGrid)
        COLS= len(obstacleGrid[0])
        cache=[[-1]*COLS for i in range(ROWS)]
        if obstacleGrid[0][0]==1 or obstacleGrid[ROWS-1][COLS-1]==1:
            return 0

        def recur(r,c):

            if r==ROWS or c==COLS or obstacleGrid[r][c]==1:
                return 0

            if r==ROWS-1 and c==COLS-1:
                return 1


            if cache[r][c]!=-1:
                return cache[r][c]

            cache[r][c]= recur(r+1, c)+ recur(r,c+1)

            return cache[r][c]

        return recur(0,0)