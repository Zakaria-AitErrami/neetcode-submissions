class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        from collections import deque
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                    visited.add((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        minutes = 0
        
        while queue:
            rotted = False
            for _ in range(len(queue)):
                R,C = queue.popleft()
                for dr,dc in directions:
                    nr,nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr==rows or nc==cols or (nr,nc) in visited or grid[nr][nc]==0:
                        continue
                    if grid[nr][nc]==1:
                        rotted = True
                        fresh-=1
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        grid[nr][nc]=2
            if rotted:
                minutes+=1
        
        return minutes if fresh==0 else -1
