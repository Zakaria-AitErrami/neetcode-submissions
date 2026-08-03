class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen:
                    return False
                if board[row][i]!='.':
                    seen.add(board[row][i])
        
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] in seen:
                    return False
                if board[i][col]!='.':
                    seen.add(board[i][col])
                    
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in squares[(i//3,j//3)]:
                    return False
                else:
                    squares[(i//3,j//3)].add(board[i][j])
        return True
