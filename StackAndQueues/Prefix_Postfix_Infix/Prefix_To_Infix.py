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

    def prefix_to_infix(self, s):
        s=s[::-1]
        return self.postfix_to_infix(s)

sol=Solution()
s= "*+ab-cd"
print(sol.prefix_to_infix(s))

# time:-O(n)
# space:-O(n)