class Solution():
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

    def fun(self, arr):
        nse = self.next_smaller_element(arr)
        pse = self.previous_smaller_element(arr)
        max_area = 0
        for i in range(len(arr)):
            right = nse[i]
            left = pse[i]
            area = (right - left - 1) * arr[i]
            max_area = max(max_area, area)
        return max_area
    
sol=Solution()
heights = [2,1,5,6,2,3]
print(sol.fun(heights))