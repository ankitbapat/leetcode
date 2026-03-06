class Solution():
    def fun(self, n):
        if n<=0: return False
        # if n==1: return True
        if n & (n-1) == 0: return True
        else: return False

sol=Solution()
n = 10
print(sol.fun(n))

# time:- O(1) - constant time bitwise operation.
# Space:- O(1)

# power of 2:-
# 2^0 - 1 -> 01
# 2^1 - 2 -> 10
# 2^2 - 4 -> 100
# 2^3 - 8 -> 1000
# 2^4 - 16 -> 10000
# 2^5 - 32 -> 100000