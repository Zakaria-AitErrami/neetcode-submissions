class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            from collections import deque
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()

                

                for dr,dc in directions:
                    R, C = row+dr, col + dc
                    if min(R,C) < 0 or R >= rows or C >= cols or grid[R][C] == "0" or (R,C) in visited:
                        continue
                    queue.append((R,C))
                    visited.add((R,C))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count +=1
        return count
