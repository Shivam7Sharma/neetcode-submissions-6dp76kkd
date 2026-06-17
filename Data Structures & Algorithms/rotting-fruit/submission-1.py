class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        q= deque()
        #visited= set()
        time=0
        ROWS, COLS= len(grid), len(grid[0])
        direct= [(1,0),(0,1),(-1,0),(0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        while fresh>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in direct:
                    nr, nc= r+dr, c+ dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr, nc))

            time+=1

        return time if not fresh else -1
