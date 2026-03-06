class Solution():
    def fun(self, n, i):
        if n & (1<<i) == 0:
            return False
        else:
            return True

sol=Solution()
n = 10
i = 1
print(sol.fun(n,i))

# time:- O(1) - constant time bitwise operation.
# Space:- O(1)