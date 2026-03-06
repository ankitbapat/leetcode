class solution:
    def fun(self, n, curr, o, c, res):
        if o==c==n:
            res.append(curr)
            return
        if o<n:
            self.fun(n, curr+"(", o+1,c, res)
        if c<o:
            self.fun(n, curr+")", o,c+1, res)

s=solution()
n=3
res=[]
s.fun(n, "", 0,0, res)
print(res)

# time:- O(2^n) - 2 choices for each branch
# space:- O(n) - stack space