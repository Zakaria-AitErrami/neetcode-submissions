class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        ilands = 0
        from collections import deque
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            visited.add((r,c))
            queue = deque()
            queue.append((r,c))

            while queue:
                R,C = queue.popleft()
                for dr, dc in directions:
                    nr, nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visited or grid[nr][nc] == "0":
                        continue
                    queue.append((nr,nc))
                    visited.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    ilands+=1
        return ilands 
                    
        