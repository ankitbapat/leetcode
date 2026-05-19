class Solution():
    def pge(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(i)
        return res
    def fun(self, n, arr):
        pge = self.pge(arr)
        ans = [0] * n
        for i in range(n):
            ans[i] = i - pge[i]
        return ans    
sol=Solution()
n = 7
arr = [120, 100, 60, 80, 90, 110, 115]
print(sol.fun(n, arr))

# time:- O(n)
# Space:- O(n)