class Solution:
    def postfix_to_infix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(f"({a}{i}{b})")
        return st[-1]

sol=Solution()
s= "ab+c*"
print(sol.postfix_to_infix(s))

# time:-O(n)
# space:-O(n)