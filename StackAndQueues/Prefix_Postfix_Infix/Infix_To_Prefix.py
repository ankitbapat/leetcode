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
    
    # Same as the Infix_toPostfix.py 
    # only one change (should we strickly less than):-
    #   (self.prec(s[i]) < self.prec(st[-1])) 
    #   instead of 
    #   (self.prec(s[i]) <= self.prec(st[-1])))
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
                while st and self.prec(s[i]) < self.prec(st[-1]):
                    res=res+st.pop()
                st.append(s[i])
                    
        while st:
            res = res+st.pop()
        return res
    
    def infix_to_prefix(self, infix):
        infix = infix[::-1] # Reverse
        infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')') # Replace '(' with ')' and vice versa
        prefix = self.infix_to_postfix(infix) # Get the postfix of the modified string
        return prefix[::-1]  # Reverse
    
sol=Solution()
s="x+y*z/w+u"
print(sol.infix_to_prefix(s))

# time:-O(n)
# space:-O(n)