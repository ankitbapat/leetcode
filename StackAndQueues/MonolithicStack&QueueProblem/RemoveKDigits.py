class Solution:
    def fun(self, num, k):
        #the intution is to keep the smaller elements at front/preceding and remove the larger elements (k larger elements)
        st = []
        if k==len(num): return "0" #edge case where we remove all elements
        for i in num:
            while k>0 and st and st[-1] > i:
                st.pop()
                k=k-1
            st.append(i)
        # edge case where no element is removed n=[1,2,3,4,5] k=2. in this case the stack will have all elements coz every preceding element is smaller. 
        # so remove the last k elements from the stack which are the largest elements.
        while st and k>0: 
            st.pop()
            k=k-1
        
        res = ""
        while st:
            res = res + st.pop()
        
        # Trimming the 0's at the top of the stack, these are the 0's which are actually at the front of the input string
        res = res.rstrip('0')
        # if res is "" return 0. This happens in case of num="10", k=1
        if not res: return "0"
        else: return res[::-1]
    
sol=Solution()
nums = "541892"
k = 2
nums = "1002991"
k = 3
print(sol.fun(nums, k))

# time:- O(n)[push and pop from stack] + O(k)[pop k larger elements from top] + O(n)[pop all elements to form result]
# space:-O(n)