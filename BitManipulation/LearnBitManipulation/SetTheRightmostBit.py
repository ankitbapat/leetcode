class Solution():
    def fun(self, n):
        return n | (n+1)

sol=Solution()
n =10
print(sol.fun(n))

# time:- O(1) - constant time bitwise operation.
# Space:- O(1)