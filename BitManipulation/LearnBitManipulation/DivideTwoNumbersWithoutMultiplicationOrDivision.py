class Solution():
    def fun(self, dividend, divisor):
        # BRUTE force:- 
        #   keep on removing divisor from dividend - untill dividend is less than divisor. 
        #   Time complexity O(dividend). If divisor is 1 and dividend is 2**31-1. Then it will lead to time limit exceed.

        # OPTIMAL approach:- 
        #   Remove the largest possible value (multiple of divisor) from the dividend first, 
        #   then remove the second-largest value (multiple of divisor) from the dividend,
        #   then remove 3rd largest ..and so on!! - untill dividend is less than divisor.
            
        #   Multiples of 3 are => 3 x 1(2^0), 3 x 2(2^1), 3 x 4(2^2), 3 x 8(2^3), 3 x 16(2^4), 3 x 32(2^5)... 
        #   So try to get the highest number/multiple of 3 and reduce it from dividend first, 
        #   then second-highest, then third highest, etc and keep reducing till devedend becomes less than divisor
        
        #   Example:- Remove 12(3*2**2) from 22, left with 10. remove 6(3*2**1), left with 4. remove 3(3*2**0), left with 1. stop. Sum (2**2 + 2**1 + 2**0) = 7

        # POINT:- THE RANGE OF NUMBERS THAT CAN BE STORED IN COMPUTER IS [-2**31 <-> 2**31-1]

        if dividend==divisor: return 1
        if divisor==1: return dividend
        if dividend == -2**31 and divisor == -1: return 2**31-1
        if divisor==-1: return -1*dividend 
        sign=1
        if (divisor<=0 and dividend>0) or (divisor>0 and dividend<=0): sign=-1       
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        while dividend >= divisor:
            n=0
            while dividend >= (divisor * 2**(n+1)): n=n+1 # THIS WILL CHNAGE TO => [ dividend >= divisor<<(n+1) ]
            # 2**n => 1<<n. why n+1 because if we took n=0 -> (divisor * 2**0 == divisor). 
            # So the check is redundant. If we do that our n increased by 1 unnecessarily. and you will get result as actual result + 1.
            
            # Also, In binary arithmetic, multiplying a number by (2^n) is equivalent to shifting its binary representation to the left by (n) positions.
            # Therefore, (3 x 2^n) is equivalent to (3<<n). 
            # For example, if (n=2): 3 x (2^2) => 3 x 4 = 12 => 3 << 2 (binary 011 shifted left by 2) = 1100 (which is 12 in decimal).
            quotient = quotient + (2**n)
            dividend = dividend - (divisor * 2**n) # THIS WILL CHNAGE TO => [ dividend = dividend - divisor<<n ]
        
        if quotient<-2**31: return -2**31
        if quotient>2**31-1: return 2**31-1
        if sign==-1: return -1*quotient
        elif sign==1: return quotient

sol=Solution()
dividend=22
divisor=3

print(sol.fun(dividend, divisor))

# 2**4 -> 16 -> 10000 -> 1<<4
# 3 x 2**4 -> 3 x 10000 -> 011 

#   Time complexity:- O((logN)^2) – 
# (where N is the absolute value of dividend). The outer loop runs for O(logN) times. The inner loop runs for O(logN) (approx.) times as well.