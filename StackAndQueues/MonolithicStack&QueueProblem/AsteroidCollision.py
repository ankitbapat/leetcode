class Solution:
    def fun(self, asteroids):
        st=[]
        for i in asteroids:
            # push all positive in stack
            if i>0:
                st.append(i)
            # for negatives - do the check with positives in stack
            else:
                while st and st[-1] > 0 and st[-1] < abs(i): # while +ve in stack and value is less -> pop()
                    st.pop()
                if st and st[-1] == abs(i): # if +ve and -ve values are same -> pop() +ves
                    st.pop()
                elif not st or st[-1] < 0: # push() only if - stack is empty, or, already a -ve in stack(same direction)
                    st.append(i)
        return st
                
sol=Solution()
asteroids = [10, 5, -3, -8, 7, -6, -7, 12, -15, 20]
print(sol.fun(asteroids))

# time and space:-O(n)