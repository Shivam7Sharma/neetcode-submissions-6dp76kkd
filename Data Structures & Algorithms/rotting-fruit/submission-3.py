class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        time=0

        rotten=deque()

        # count fresh and get index of rotten
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y]==1:
                    fresh+=1
                elif grid[i][y]==2:
                    rotten.append((i,y))
        
        dire=[(1,0),(0,1),(-1,0),(0,-1)]

        # if deque mutatates in the loop then loop on the initial size of deque

        while rotten and fresh>0:
            for n in range(len(rotten)):            
                i,y=rotten.popleft()
                
                for di, dy in dire:
                    ni=i+di
                    ny=y+dy
                    if 0<=ni<len(grid) and 0<=ny<len(grid[0]) and grid[ni][ny]==1:
                        fresh-=1
                        rotten.append((ni,ny))
                        grid[ni][ny]=2
            
            time+=1


        return -1 if fresh else time
            
