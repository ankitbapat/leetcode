class Solution():
    def fun(self, matrix, word):

        def dfs(r ,c, index):
            if index==len(word): return True
            
            if r not in range(0,ROWS) or c not in range(0,COLS) or ((r,c) in st) or matrix[r][c]!=word[index]: 
                return False
            
            st.add((r,c))
            res = dfs(r,c+1,index+1) or dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c-1,index+1)
            st.remove((r, c))

            return res
        
        ROWS=len(matrix)
        COLS=len(matrix[0])
        st=set()
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False

        

s=Solution()
word = "ABCCED"
matrix = [["A", "B", "C", "E"], 
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
print(s.fun(matrix, word))

# Time:- O(n^2)*O(4^len(word)) - using 2 for loops + 4 choises at each element during recursion.
# space:- O(len(word)) + O(set) - recurion depth + used space for SET


#Approach2:- Mark the matrix in-place. So not SET required for storing the values
class Solution():
    def fun(self, matrix, word):

        def dfs(r ,c, index):
            if index==len(word): return True
            
            if r not in range(0,ROWS) or c not in range(0,COLS) or matrix[r][c]!=word[index]: 
                return False
            
            temp = matrix[r][c]
            matrix[r][c]="#"

            res = dfs(r,c+1,index+1) or dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c-1,index+1)
        
            matrix[r][c]=temp

            return res
        
        ROWS=len(matrix)
        COLS=len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False

        

s=Solution()
word = "ABCCED"
matrix = [["A", "B", "C", "E"], 
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
print(s.fun(matrix, word))

# Time:- O(n^2)*O(4^len(word)) - using 2 for loops + 4 choises at each element during recursion.
# space:- O(len(word)) - recurion depth