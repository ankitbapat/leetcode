class Solution:
    def fun(self, arr):
        st=[]
        res=[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and st[-1] >= arr[i]:
                st.pop()
            if st:  res[i] = st[-1]
            else: res[i] = -1
            st.append(arr[i])
        return res
sol=Solution()
arr=[4, 8, 5, 2, 25]
arr=[10, 9, 8, 7]
print(sol.fun(arr))

# time and space:- O(n)