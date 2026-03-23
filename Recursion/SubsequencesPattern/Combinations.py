class Solution():
    def fun(self, curr, start):
        if len(curr)==k:
            res.append(curr.copy())
            return
        for i in range(start,n+1):
            curr.append(i)
            self.fun(curr, i+1)
            curr.pop()
        
sol=Solution()
n=4
k=2
res=[]
sol.fun([], 1)
print(res)

  
#same/similar as combination sum 2, where we choose ith element then iterate over i+1 till n elements to choose from.
# Time:- 2**n * k - same as combination sum 2
# space:- k * x - same as combination sum 2


# [1,2,3,4]

# [1]                 [2]             [3]
# [1,2] [1,3] [1,4]   [2,3] [2,4]     [3,4] 