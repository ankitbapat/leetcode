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

    def histogram(self, arr):
        nse = self.next_smaller_element(arr)
        pse = self.previous_smaller_element(arr)
        max_area = 0
        for i in range(len(arr)):
            right = nse[i]
            left = pse[i]
            area = (right - left - 1) * arr[i]
            max_area = max(max_area, area)
        return max_area

    def fun(self, matrix):
        height=[0]*len(matrix[0])
        final_max_area=0
        for row in matrix:
            for c in range(len(row)):
                if row[c]=="1": height[c] = height[c]+1
                else: height[c] = 0
        
            current_max_area = self.histogram(height)
            final_max_area = max(final_max_area, current_max_area)
        return final_max_area
    
sol=Solution()
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print(sol.fun(matrix))

# time:- O(n*m + n*N) - O(n*m) is O(row*col) -> to iterate through each element in matrix. Also O(N) for histogram max_area finder
# space:- O(n)