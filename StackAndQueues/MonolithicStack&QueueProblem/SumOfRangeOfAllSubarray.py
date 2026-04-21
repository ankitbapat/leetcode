class Solution:
    #Optimal
    def nge(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = n
            st.append(i)
        return res
    def pge(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(i)
        return res
    
    def nse(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = n
            st.append(i)
        return res
    def pse(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(i)
        return res
    
    def total_small(self, arr):
        total=0
        nse = self.nse(arr)
        pse = self.pse(arr)
        for i in range(len(arr)):
            left = (i-pse[i]) 
            right = (nse[i]-i)
            val = left * right * arr[i] #no of subsets where i in smaller * arr[i]
            total = total + val
        return total
    
    def total_large(self, arr):
        total=0
        nge = self.nge(arr)
        pge = self.pge(arr)
        for i in range(len(arr)):
            left = (i-pge[i])
            right = (nge[i]-i) 
            val = left * right * arr[i]  #no of subsets where i in larger * arr[i]
            total = total + val
        return total

    def fun(self, arr):
        return self.total_large(arr) - self.total_small(arr)
        
    
sol=Solution()
arr=[4, -2, -3, 4, 1]
print(sol.fun(arr))

# time:- O(10n)
# space :- O(8n)