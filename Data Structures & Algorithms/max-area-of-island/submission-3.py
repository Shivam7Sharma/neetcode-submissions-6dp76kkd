class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])
        direc=[(1,0),(0,1),(-1,0),(0,-1)]
        area=0
        # Use Bottom up approach by returning from dfs 
        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]!=1:
                return 0

            grid[r][c]=-1
            area=1
            for dr, dc in direc:
                area+=dfs(dr+r, dc+c)

            return area

        maxarea=0
        for r in range(ROWS):
            for c in range(COLS):
                area=0
                if grid[r][c]==1:
                    area=dfs(r,c)
                    maxarea= max(area, maxarea)

        return maxarea


            