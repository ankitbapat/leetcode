class Solution:
    #Brute
    def fun(self, arr):
        n = len(arr)
        res=0
        for i in range(n):
            min=arr[i]
            for j in range(i, n):
                if arr[j] < min: min=arr[j]
                res=res+min
                # print(arr[i: j+1], min)
        return res
    # time:- O(n^2), space:- O(1)
    
    #Optimal
    def next_smaller_element(self, arr):
        st=[]
        n = len(arr)
        res=[0]*n
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: res[i] = st[-1] 
            else: res[i] = n
            st.append(i)
        return res
    
    def previous_smaller_element(self, arr):
        st=[]
        n = len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st: res[i] = st[-1] 
            else: res[i] = -1
            st.append(i)
        return res
    
    def fun_opt(self, arr):
        nse = self.next_smaller_element(arr)
        pse = self.previous_smaller_element(arr)
        total = 0
        mod = int(1e9 + 7)
        for i in range(len(arr)):
            right = (nse[i] - i)
            left = (i - pse[i])
            val = (left * right * arr[i])
            total = total + val
        return total % mod

    # time:- O(2n) + O(2n) + O(n) = O(5n) = O(n)
    # space:- O(4n) = O(n)

sol=Solution()
arr=[3, 1, 2, 5]
print(sol.fun(arr))
print(sol.fun_opt(arr))