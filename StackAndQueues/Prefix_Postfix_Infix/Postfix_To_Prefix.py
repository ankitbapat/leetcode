class Solution:
    def postfix_to_prefix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(f"{i+a+b}")
        return st[-1]

sol=Solution()
s= "abc*+d-"
print(sol.postfix_to_prefix(s))

# time:-O(n)
# space:-O(n)