class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        ROWS= len(image)
        COLS= len(image[0])
        if image[sr][sc]==color:
            return image

        def dfs(original_color, row, col, color):
            if 0<=row<ROWS and 0<=col<COLS and image[row][col]==original_color:
                image[row][col]=color

                dfs(original_color, row+1, col, color)
                dfs(original_color, row, col+1, color)
                dfs(original_color, row-1, col, color)
                dfs(original_color, row, col-1, color)

            return image

        return dfs(image[sr][sc], sr,sc, color)