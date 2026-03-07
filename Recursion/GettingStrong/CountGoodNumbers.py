class Solution():
    def fun(self,n):
        MOD = 10**9+7
        even_places = (n+1)//2          # Ceiling of n/2
        odd_places = n//2               # Floor of n/2
        return ( pow(5, even_places, MOD) * pow(4, odd_places, MOD) ) % MOD

sol=Solution()
n=50
print(sol.fun(n))
# Simple code understand from AlgoMonster website. https://algo.monster/liteproblems/1922
# Time:- log(n) -  This is because the built-in pow function with three arguments uses fast exponentiation (also known as exponentiation by squaring) 
# to compute the modular exponentiation