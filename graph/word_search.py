class Solution:
    def __init__(self):
        self.row=0
        self.col=0
    def check(self, board, i,j,word):
        if len(word)==0:
            return True
        if i<0 or i==self.row or j<0 or j==self.col or board[i][j]!=word[0]:
            return False
        res=False
        board[i][j]="#"
        for row,col in [(1,0),(-1,0),(0,-1),(0,1)]:
            res= self.check(board, i+row,j+col,word[1:])
            if res:
                break
        board[i][j]=word[0]
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row=len(board)
        self.col=len(board[0])
        for i in range(self.row):
            for j in range(self.col):
                if self.check(board, i, j,word):
                    return True
        return False
    