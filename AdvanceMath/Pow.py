class Solution:
    def fun(self,x,n):
        res=1
        while n>0:
            if n%2==1: #odd
                res=res*x
                n=n-1
            else: #even
                n=n/2
                x=x*x
        return res
    def main(self, x,n):
        if n<0: return 1/self.fun(x,abs(n))
        else: return self.fun(x,abs(n))

sol=Solution()
x = 2
n = 10
print(sol.main(x,n))

# Time Complexity: O(log(n))
# Space Complexity: O(log(n))