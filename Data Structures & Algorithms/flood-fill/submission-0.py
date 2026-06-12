class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        def dfs(image, sr, sc, color, original, visited):
            if min(sr,sc)<0 or sr==len(image) or sc==len(image[0]) or (sr,sc) in visited:
                return
            if image[sr][sc]==original:
                visited.add((sr,sc))
                image[sr][sc]=color

                dfs(image, sr+1,sc,color, original,visited)
                dfs(image, sr,sc+1,color, original,visited)
                dfs(image, sr-1,sc,color, original,visited)
                dfs(image, sr,sc-1,color, original,visited)

                return

        dfs(image, sr,sc, color, image[sr][sc], set())

        return image