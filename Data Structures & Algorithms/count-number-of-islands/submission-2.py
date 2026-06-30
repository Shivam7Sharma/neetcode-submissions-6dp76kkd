class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])


        def dfs(row, col):
            if 0<=row<ROWS and 0<=col<COLS and grid[row][col]=="1":
                grid[row][col]="0"
                dfs(row+1,col)
                dfs(row,col+1)
                dfs(row-1, col)
                dfs(row, col-1)
                return 1
            else:
                return 
        island=0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]=="1":
                    dfs(row, col)
                    island+=1

        return island


            