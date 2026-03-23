# brute force
class Solution():
    def fun(self, item):
        curr=[]
        for p in range(1,item+1):
            if item % p == 0: #if item is divisible by p
                curr.append(p) #add p in curr
        return curr
    
sol=Solution()
item = 36
print(sol.fun(item))
# time:- O(n)
# space:- O(n)

# optimal force
import math
class Solution():
    def fun(self, item):
        curr=[]
        for p in range(1, int(math.sqrt(item))+1):
            if item % p == 0: 
                curr.append(p)
                if item//p != p: #to get rid of duplicate 6.
                    curr.append(item//p)

        return curr
    
sol=Solution()
item = 36
print(sol.fun(item))
# time:- O(sqrt(n))
# space:- O(n)