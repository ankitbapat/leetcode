class Solution:
    def isprime(self, item):
        for i in range(2, item):
            if item % i == 0: return False
        return True
    def countPrimes(self, n):
        if n==0 or n==1: return 0
        c=0
        for i in range(2, n):
            if self.isprime(i):
                c = c + 1
        return c
    
sol=Solution()
number=10
print(sol.countPrimes(number))

# time:- O(n) * O(n) -> one to traverse and another to find prime
# space:- O(1)

# How can we improve this. One possibility is to get the prime number will traversing from 2 till sqrt of n. Instead of 2 till n:-
# def isprime(self, item):
#     for i in range(2, math.sqrt(item)):
#         if item % i == 0: return False
#     return True

# Another approach optimal one is to get the isPrime() down to O(1). We will maintain a black box which will return us isPrime() in O(1).
# To get this in O(1) we use "Sieve of Eratosthenes" algo. 
# How? - In this we maintain a record for each number from 2 till n, That record will provide us if a number is a prime or not in O(1) time.
# So lets say if we have an array and we could mark all the prime numbers from 2 till n in that array. and then return the array elements which are marked.
# This would give us all the primes from 2 till n.

#Optimal:- also see the striver's video
import math
class Solution:
    def getprime(self, item):
        arr=[1] * (item+1) #initiaize array elements with 1 / set all of them
        
        for i in range(2, int(math.sqrt(item))+1): # we do not need to traverse till n. for example lets say n is 30. and i is 7. 
            # for the inner loop -> j=i*i=49 and j<=30. so the inner loop never runs. that is why we traverse i from 2 till sqrt(n)
            if arr[i]==1:
                for j in range(i*i, item+1, i): 
                    # for e.g the i==5. so we do not need 5*2,5*3,5*4... because they are already computed. 
                    # we need from 5*5 so we have i*i (see striver video for its explaination)
                    #and we jump by i to get multiples of i.
                    arr[j]=0
        c=0
        for i in range(2, item+1): #return all set elements in that array
            if arr[i]==1: c=c+1
        return c
        
    def countPrimes(self, n):
        if n==0 or n==1: return 0
        return self.getprime(n)
                
    
sol=Solution()
number=10
print(sol.countPrimes(number))

# time:- O(n) + O(log(logn)) + O(n) -> one to set array to 1. another O(log(logn)) to find primes. another O(n) to return items that are only 1's
# space:- O(n) - to hold the array
