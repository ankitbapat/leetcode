
class Solution:
    #brute
    def fun_brute(self, arr):
        res=[-1] * len(arr)
        for i in range(len(arr)):
            item = arr[i]
            j=(i+1) % len(arr)
            while j != i:
                if arr[j] > item:
                    res[i] = arr[j]
                    break
                j=(j+1) % len(arr)
        return res

    # time:- O(n^2)
    # space:- O(n)
    
    # optimal
    def fun_opt(self, arr):
        st=[]
        n=len(arr)
        res=[-1]*n
        
        for i in range(2*n-1, -1,-1):
            current_element = arr[i % n]
            while st and st[-1] <= current_element:
                st.pop()
            if i < n:
                if st: res[i] = st[-1]
                else: res[i] = -1
            st.append(current_element)
        
        return res
    
    # time:- O(4n) -> outerloop - 2n & inner while loop will run only O(2n) time in total. (same explanation as next_greater_element_1)
    # space:- O(2n)

sol=Solution()
arr = [2, 10, 12, 1, 11]
print(sol.fun_brute(arr))
print(sol.fun_opt(arr))