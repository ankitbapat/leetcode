class Solution:
    def fun(self, arr):
        res=0
        l=0
        r=len(arr)-1
        leftMax=0
        rightMax=0
        while l<=r:
            if arr[l]<=arr[r]:
                if arr[l]>leftMax: leftMax=arr[l]
                else: res=res+leftMax-arr[l]
                l=l+1
            else:
                if arr[r]>rightMax: rightMax=arr[r]
                else: res=res+rightMax-arr[r]
                r=r-1
        return res

sol=Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.fun(height))

# time:- O(n)
# space:- O(1)