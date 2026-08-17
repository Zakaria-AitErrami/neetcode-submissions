from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        seen_pc = set()
        seen_at = set()
        queue_pc = deque()
        queue_at = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        rows, cols = len(heights), len(heights[0])

        for c in range(cols):
            seen_pc.add((0,c))
            queue_pc.append((0,c))
        for r in range(rows):
            seen_pc.add((r,0))
            queue_pc.append((r,0))

        for r in range(rows):
            seen_at.add((r,cols-1))
            queue_at.append((r,cols-1))
        
        for c in range(cols):
            seen_at.add((rows-1,c))
            queue_at.append((rows-1,c))
        
        def getCords(queue, seen):
            
            while queue:
                R,C = queue.popleft()
                for dr, dc in directions:
                    nr, nc = R+dr, C+dc
                    if min(nr,nc) < 0 or nr >= rows or nc >= cols or (nr,nc) in seen:
                        continue
                    if heights[nr][nc] >= heights[R][C]:
                        queue.append((nr,nc))
                        seen.add((nr,nc))
                        
            return seen
        
        cords_at = getCords(queue_at, seen_at)
        cords_pc = getCords(queue_pc, seen_pc)

        return list(cords_at & cords_pc)





        