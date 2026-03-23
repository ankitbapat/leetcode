
# brute force
class Solution():
    def getPrimeFactorization(self, item):
        # while item is getting divided by 2 keep on dividing by 2.
        # If not then try 3, if not then try 5 , if not then try 7, then 13, and so on..
        curr=[]
        for p in range(2,item+1):
            while item % p == 0: #while item is divisible by p
                item = item / p #divide the item by p
                curr.append(p) #add p in curr
        return curr
    
    def fun(self,q):
        res=[]
        for item in q:
            res.append(self.getPrimeFactorization(item))
        return res
                 
sol=Solution()
queries = [2, 3, 4, 5, 6]
queries = [7, 12, 18, 780]
print(sol.fun(queries))

# time:-(O(item)*O(logn)) * O(N) -> N is size of queries, O(item) is the (2->item+1) loop. logn for inner while loop
# space:-O(log(item)) list stores the prime factors. The number of prime factors for any number log(number)

#Explanation:-
#This code works because it uses the Trial Division algorithm, specifically designed for prime factorization. 
# It does not need to explicitly check if a divisor is prime because the algorithm guarantees that only prime numbers are appended to the result list

# By starting from p=2 and working upwards, 
# the code ensures that if a composite number (like 4, 6, or 9) tries to divide the number item, it can't, 
# because all the smaller prime factors that make up that composite number have already been divided out

# Example (12):
# p=2: 
#  curr=[2], item becomes 6.
# p=2: 
#  curr=[2, 2], item becomes 3.
# p=2: 
#  cannot divide by 2
#  curr=[2, 2], item becomes 3.
#  (Skip 2).
# p=3: 
#  curr=[2, 2, 3], item becomes 1.
# Result: [2, 2, 3]. Note that 4 (which is 

# Note that 4 (which is (2x2)) was never added, only the constituent primes. 


#optimal:- Striver video
import math
class Solution():
    def getPrimeFactorization(self, item):
        # while item is getting divided by 2 keep on dividing by 2.
        # If not then try 3, if not then try 5 , if not then try 7, then 13, and so on..
        curr=[]
        for p in range(2, int(math.sqrt(item))+1): # the code still works if we just iterate it till sqrt(item).
            while item % p == 0: #while item is divisible by p
                item = item / p #divide the item by p
                curr.append(p) #add p in curr
        if item!=1: curr.append(int(item)) # we need to add the last prime number which divides the item completely. see striver video for this last statement
        return curr
    
    def fun(self,q):
        res=[]
        for item in q:
            res.append(self.getPrimeFactorization(item))
        return res
                 
sol=Solution()
queries = [2, 3, 4, 5, 6]
queries = [7, 12, 18, 780]
print(sol.fun(queries))
# time:-O(sqrt(item) * logn) * O(N) -> N is size of queries, O(sqrt(item)) is the (2->sqrt(item)+1) loop. and logn for the inner while loop
# space:-O(log(item)) list stores the prime factors. The number of prime factors for any number log(number)