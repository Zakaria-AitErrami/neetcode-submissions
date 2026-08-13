class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        from collections import deque
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visited.add((r,c))
                    queue.append((r,c))
        dst = 1
        while queue:
            
            for i in range(len(queue)):
                R,C = queue.popleft()
                for dr,dc in directions:
                    nr,nc = R+dr, C+dc
                    if min(nr,nc) < 0 or(nr,nc) in visited or nr==rows or nc==cols or grid[nr][nc]==-1:
                        continue
                    visited.add((nr,nc))
                    queue.append((nr,nc))
                    grid[nr][nc]= dst
            dst+=1


