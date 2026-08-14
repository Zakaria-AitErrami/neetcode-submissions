class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs(r,c):
            from collections import deque
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                R,C = queue.popleft()
                for dr, dc in directions:
                    nr, nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or grid[nr][nc]=="0":
                        continue
                    visited.add((nr,nc))
                    queue.append((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        
        return count