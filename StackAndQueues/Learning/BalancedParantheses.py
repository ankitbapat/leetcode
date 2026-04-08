class Solution:
    def fun(self, s):

        st = []
        for i in range(len(s)):            
            if s[i] == "(" or s[i] == "[" or s[i] == "{": st.append(s[i])
            else:
                if st:
                    val = st.pop()
                    if (s[i]==")" and val != "(") or (s[i]=="]" and val != "[") or (s[i]=="}" and val != "{") : return False
                else: return False
        return True if len(st)==0 else False

sol = Solution()
s = "()[{}()]"
print(sol.fun(s))

# time:- O(n)
# space:- O(n)