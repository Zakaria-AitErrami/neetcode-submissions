class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(r,c):
            visited.add((r,c))
            queue = deque()
            queue.append((r,c))
            count = 1
            while queue:
                R,C = queue.popleft()
                for dr,dc in directions:
                    nr,nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc]==0 or (nr,nc) in visited:
                        continue
                    count+=1
                    visited.add((nr,nc))
                    queue.append((nr,nc))
            return count

                


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==1 and (r,c) not in visited:
                    res = max(res,bfs(r,c))
        return res