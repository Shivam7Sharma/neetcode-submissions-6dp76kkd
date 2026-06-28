class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        direc=[(-1,-1),(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,1),(1,-1)]
        ROWS= len(grid)
        COLS= len(grid[0])
        if grid[ROWS-1][COLS-1] ==1 or grid[0][0]==1:
            return -1
        length=0
        q=deque()
        q.append((0,0,1))
        visited= set()
        visited.add((0,0))
        

        while q:
            i,y, length= q.popleft()
            
            if (i,y)==(ROWS-1, COLS-1):
                return length
            for di, dy in direc:
                ni= i+di
                ny= y+dy
                if 0<=ni<ROWS and 0<=ny<COLS and grid[ni][ny]==0 and (ni,ny) not in visited:
                    q.append((ni,ny, length+1))
                    visited.add((ni,ny))

        return -1


