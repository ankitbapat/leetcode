class Solution:
    def myAtoi(self, s):
        s=s.lstrip(" ")
        sign=1
        i=0
        res=0
        if s=="": return res
        if s[i]=="+":
            sign=1
            i=i+1
        elif s[i]=="-":
            sign=-1
            i=i+1
        
        def rec(i,res):
            if i>=len(s) or not s[i].isdigit(): return res
            res=res*10 + int(s[i])
            return rec(i+1, res)
        res = rec(i,res)
        
        # while i<len(s) and s[i].isdigit():
        #     res=res*10 + int(s[i])
        #     i=i+1
        
        if sign==-1: res=res*-1
        if res>2**31-1:return 2**31-1
        elif res<-2**31: return -2**31
        else: return res

sol=Solution()
s = "1337c0d3"
print(sol.myAtoi(s))

# Time Complexity: O(n)
# Space Complexity: O(n)