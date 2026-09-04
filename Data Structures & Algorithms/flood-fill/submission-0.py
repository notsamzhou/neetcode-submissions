class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = set()
        def dfs(i, j, original):
            if not 0 <= i < len(image) or not 0 <= j < len(image[0]) or image[i][j] != original or (i, j) in visited:
                return

            visited.add((i, j))
            image[i][j] = color

            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                dfs(ni, nj, original)


        dfs(sr, sc, image[sr][sc])

        return image
        