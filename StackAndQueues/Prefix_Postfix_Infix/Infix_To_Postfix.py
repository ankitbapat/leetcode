class Solution:
    def prec(self, c):
        if c == '^':
            return 3
        elif c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1
    def infix_to_postfix(self, s):
        res=""
        st=[]
        for i in range(len(s)):
            if s[i].isalnum(): res = res + s[i]
            elif s[i]=="(":
                st.append(s[i])
            elif s[i]==")":
                while st and st[-1]!="(":
                    res=res+st.pop()
                st.pop() # throw the "("
            else:
                while st and self.prec(s[i]) <= self.prec(st[-1]):
                    res=res+st.pop()
                st.append(s[i])
                    
        while st:
            res = res+st.pop()
        return res

sol=Solution()
s="a+b*(c^d-e)^(f+g*h)-i"
print(sol.infix_to_postfix(s))

# time:-O(n)
# space:-O(n)