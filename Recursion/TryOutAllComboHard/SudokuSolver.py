class Solution():
    def check(self, r,c,v):
        # for this check see the solution from apna college
        for j in range(9):
            if board[r][j] == v:
                return False #check next number in values, and also skip row and small-matrix check
        for i in range(9):
            if board[i][c] == v:
                return False #check next number in values, and also skip row and small-matrix check
        sr=3*int(r/3)
        sc=3*int(c/3)
        for i in range(sr, sr+3):
            for j in range(sc, sc+3):
                if board[i][j] == v:
                    return False #check next number in values, and also skip row and small-matrix check
        return True


    def fun(self, board): 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    for v in values:
                        if self.check(r,c,v):
                            board[r][c]=v
                            if self.fun(board): return True
                            board[r][c]="."
                    return False
        return True #base case
                    


sol=Solution()
board = [
    [5,3,".", ".",7,".", ".", ".", "."],
    [6,".",".", 1,9,5, ".", ".", "."],
    [".",9,8, ".", ".", ".", ".",6,"."],
    [8,".",".", ".",6,".", ".", ".",3],
    [4,".",".", 8,".",3, ".", ".",1],
    [7,".",".", ".",2,".", ".", ".",6],
    [".",6,".", ".", ".", ".", 2,8,"."],
    [".",".",".", 4,1,9, ".", ".",5],
    [".",".",".", ".",8,".", ".",7,9]
]
values = [1,2,3,4,5,6,7,8,9]
COLS=len(board[0])
ROWS=len(board)
print(sol.fun(board))
print(board)

# time:- O(9^n**2) + O(n**2). 9 digits to choose. 9 branches of a decision tree. for every element in a matrix -> n**2. O(n**2) for checking function.
# Space:- O(1) - only same board is modified. I think the recurion depth is n**2. since what if all elements are "." ina matrix - then we try every element.
# So the depth could be n**2
