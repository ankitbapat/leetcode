class Solution():
    def fun(self,r,c,curr):
        if r==n-1 and c==n-1:
            res.append(curr)
            return
        
        if r<0 or c<0 or r>=n or c>=n or ((r,c) in st) or grid[r][c] == 0: return

        st.add((r,c))
        self.fun(r,c+1, curr+"R") or self.fun(r,c-1, curr+"L") or self.fun(r+1,c, curr+"D") or self.fun(r-1,c, curr+"U")
        st.remove((r,c))


sol=Solution()
n=4
st=set()
grid = [ 
    [1, 0, 0, 0],
    [1, 1, 0, 1], 
    [1, 1, 0, 0], 
    [0, 1, 1, 1] 
]
res=[]
if grid[0][0] == 1: 
    sol.fun(0,0,"")
print(res)

# time:- O(4^N*M) - N*M are the positions. At reach position the mouse takes 4 directions. 4^N*M
# space:- O(N*M) - stack space