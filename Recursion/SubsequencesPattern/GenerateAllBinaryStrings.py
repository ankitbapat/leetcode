class solution:
    def fun(self, n, curr):
        if len(curr) == n: 
            res.append(curr)
            return

        self.fun(n, curr+"0")
        #1 should be added when curr is empty
        if curr == "":
            self.fun(n, curr+"1")
        #1 should not be added when curr already has elements and last element is 1
        if curr and curr[-1]!="1" : 
            self.fun(n, curr+"1")
        

s=solution()
n=3 #3
res=[]
curr=""
s.fun(n, curr)
print(res)

# Just print all the combinations. This is similar to power set or print all subsequence - choose 1 or 0.
class solution:
    def fun(self, n, curr):
        if len(curr) == n: 
            res.append(curr)
            return

        self.fun(n, curr+"0")
        self.fun(n, curr+"1")
        

s=solution()
n=3 #3
res=[]
curr=""
s.fun(n, curr)
print(res)


# Time:- O(2^n) - all possible combinations
# Space:- O(n) - stack size