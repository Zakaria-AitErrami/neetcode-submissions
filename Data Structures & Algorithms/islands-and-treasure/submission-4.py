class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    queue.append((r,c))
                    visited.add((r,c))
        dst = 1
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            for _ in range(len(queue)):
                R,C = queue.popleft()
                for dr, dc in directions:
                    nr,nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr==rows or nc==cols or grid[nr][nc]==-1 or (nr,nc) in visited:
                        continue
                    visited.add((nr,nc))
                    grid[nr][nc]=dst
                    queue.append((nr,nc))
            dst+=1
