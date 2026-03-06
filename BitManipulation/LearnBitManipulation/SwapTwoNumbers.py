class Solution():
    def fun(self, a,b):
        a=a^b
        b=a^b
        a=a^b
        return a,b
sol=Solution()
a=10
b=9
print(sol.fun(a,b))

# time:- O(1) - constant time bitwise operation.
# Space:- O(1)

# XOR removes the same numbers (same bits -> 0)
# step1:- a = a^b
# step2:- b = (a^b)^b. So b becomes a. same two b's are cancelled
# step3:- a = (a^b)^(a). Here a is a^b from step 1 and b=a from step 2. So a becomes b since 2 a's are cancelled
