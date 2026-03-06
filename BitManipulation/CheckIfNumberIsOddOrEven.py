class Solution():
    def fun(self, n):
        return False if (n & 1 == 0) else True
        # return False if (n % 2 != 0) else True

sol=Solution()
n = 10
print(sol.fun(n)) # return true for odd, false for even

# time:- O(1) - constant time bitwise operation.
# Space:- O(1)

# 1-01
# 2-10
# 3-011
# 4-100
# 5-101
# 6-110
# always last bit is 1 in case of odd and 0 in case of even