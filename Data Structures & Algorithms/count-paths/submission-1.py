class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def recur(r,c,ROWS, COLS, cache):
            if r==ROWS or c==COLS:
                return 0
            elif r==ROWS-1 and c==COLS-1:
                return 1
            else:
                if cache[r][c]:
                    return cache[r][c]
                cache[r][c]=recur(r+1,c, ROWS,COLS, cache) + recur(r,c+1,ROWS, COLS, cache)
                return cache[r][c]



        return recur(0,0,m, n, [[0]*n for i in range(m)])