class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(r,c):
            from collections import deque
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            res = 0

            while queue:
                R,C = queue.popleft()
                for dr,dc in directions:
                    nr,nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr >=ROWS or nc >= COLS or grid[nr][nc]=="0" or (nr,nc) in visited:
                        continue
                    queue.append((nr,nc))
                    visited.add((nr,nc))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1 
        return count

