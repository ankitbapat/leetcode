class Solution():
    def fun(self, start,goal):
        val = start ^ goal #get number of bits that differ
        #count number of set bits
        c=0
        while val>0:
            val = val & (val-1)
            c=c+1
        return c
sol=Solution()
start=10
goal=7
print(sol.fun(start,goal))

# time:- O(1) - constant time bitwise operation.
# Space:- O(1)