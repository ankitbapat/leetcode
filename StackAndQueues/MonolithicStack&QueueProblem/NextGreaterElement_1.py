
class Solution:
    #brute
    def fun_brute(self, arr):
        res=[-1] * len(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    res[i] = arr[j]
                    break
        return res

    # time:- O(n^2) - 2 loops - outer + inner
    # space:- O(n) - res
    
    #optimal
    def fun_opt(self, arr):
        st=[]
        res=[-1]*len(arr)
        for i in range(len(arr)-1, -1,-1):
            while st and st[-1] <= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(arr[i])
        return res
    
    # time:- O(2n) - the inner while loop will run only O(n) time in total. 
    # For each element, inner while loop (pop()) will run maximum of 1 time. Test this with decreasing number [5,4,3,2,1]. this is the worst time complexity example
    # our stack will hold all the numbers.
    # space:- O(2n) - res + stack

sol=Solution()
arr = [1, 3, 2, 4]
print(sol.fun_brute(arr))
print(sol.fun_opt(arr))