# Brute force
class Solution():
    def fun(self, n):
        c=0
        for i in range(n):
            if n & (1<<i) != 0:
                c=c+1
        return c

sol=Solution()
n =10
print(sol.fun(n))

# time:- O(log(n)) - because each bit of the integer is checked once.
# Space:- O(1)
# n = 5 = 101 -> 2


# optimal - Brian Kernighan's Algorithm 
class Solution():
    def fun(self, n):
        c=0
        while n>0:
            n = n & (n-1)  # Turn off the rightmost/smallest set bit
            c=c+1
        return c

sol=Solution()
n =10
print(sol.fun(n))

# time:- O(k) - number of set bits.
# Space:- O(1)