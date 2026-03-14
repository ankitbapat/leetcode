class Solution():
    def fun(self, L, R):
        res=0
        for i in range(L,R+1):
            res=res ^ i
        return res
sol=Solution()
L=3
R=5
print(sol.fun(L,R))

# Time:-O(n) space:O(1)

class Solution():
    # func to find xor from 1 to n
    def help(self,n):
        if n%4==1: return 1
        elif n%4==2: return n+1
        elif n%4==3: return 0
        elif n%4==0: return n
    def fun(self, L, R):
        return help(L-1) ^ self.help(R)
sol=Solution()
L=3
R=5
print(sol.fun(L,R))

# Time:-O(1) space:O(1)