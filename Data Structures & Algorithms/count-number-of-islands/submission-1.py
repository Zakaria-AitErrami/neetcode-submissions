class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        lands = 0
        def dfs(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r,c) in visited:
                return

            visited.add((r,c))
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    dfs(r, c)
                    lands+=1

        return lands
            
