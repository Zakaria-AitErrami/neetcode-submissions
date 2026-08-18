from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # capture everything except surrounded regions
        # reverse thinking
        queue = deque()
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set()

        for c in range(cols):
            if board[0][c]=="O":
                queue.append((0,c))
                seen.add((0,c))
            if board[rows-1][c]=="O":
                queue.append((rows-1,c))
                seen.add((rows-1,c))
                
        
        for r in range(1,rows-1):
            if board[r][0]== "O":
                queue.append((r,0))
                seen.add((r,0))
            if board[r][cols-1]=="O":
                 queue.append((r,cols-1))
                 seen.add((r,cols-1))
        
        # change regions of O at the edges to T
        while queue:
            R,C = queue.popleft()
            board[R][C] = "T"
            for dr,dc in directions:
                nr, nc = R+dr, C+dc
                if min(nr,nc) < 0 or nr==rows or nc == cols or board[nr][nc]=="X" or (nr,nc) in seen:
                    continue
                if board[nr][nc]=="O":
                    queue.append((nr,nc))
                    seen.add((nr,nc))
        
        # change all O in X => now every O remaining is a surrounded region
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        for r,c in seen:
            board[r][c]="O"

