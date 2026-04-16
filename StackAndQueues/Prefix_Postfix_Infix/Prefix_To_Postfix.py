class Solution:
    def postfix_to_prefix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(f"{a+b+i}")
        return st[-1]
    
    def prefix_to_postfix(self, s):
        s=s[::-1]
        return self.postfix_to_prefix(s)

sol=Solution()
s= "*+ab-cd"
print(sol.prefix_to_postfix(s))

# time:-O(n)
# space:-O(n)