# Bitwise Concepts
### Decimal to Binary
    Divide the number repeatably by 2 till quotient reaches 1. 
        13 / 2 = 6 remainder 1
        6 / 2 = 3 remainder 0
        3 / 2 = 1 remainder 1
        1 / 2 = 0 remainder 1
    13 -> 1101
### Binary to Decimal
    Each bit is multiplied by 2 raised to the power of its position index. 
        1 * 2^0 = 1
        0 * 2^1 = 0
        1 * 2^2 = 4
        1 * 2^3 = 8
    1011 -> 8+2+1 (13)
### One's complement
    Binary of 13     : 0000 1101
    One's Complement : 1111 0010
### Two's complement
    We take the 2's complement of a binary number primarily to represent signed negative numbers
        One's Complement : 1111 0010
        Add 1            : 1111 0011
### AND (&)
    13: 1101
    7:  0111
    & : 0101 → 5
### OR (|)
    13: 1101
    7:  0111
    | : 1111 → 15
### XOR (^)
    If bits differ, the result is 1; if the same, result is 0.
        13: 1101
        7:  0111
        ^ : 1010 → 10
### NOT (~)
    5:  0000 0101
    ~5: 1111 1010 → -6 (in two's complement)
### Right Shift (>>) 
    Shifts bits to the right by 1 position, fills left with 0s. This is O(1) time n space
        13(1101) >> 1 => 1101 >> 1 => 0110 → 6
### Left Shift (<<) 
    Shifts bits to the left by 1 position, fills right with 0s. This is O(1) time n space
        13(1101) << 1 => 1101 << 1 => 11010 → 26

<br>

# Tricks for BitManipulation
### Check if the i-th Bit is Set
    if num & (1<<i) == 0: return "Not set"
    else: return "Yes it is set"  
    
    - Time:- O(1). Space:- O(1)
    - Move the bit to ith position and then do (&) with num's ith bit.
### Set the i-th Bit
    return num | (1 << i).

    - Time:- O(1). Space:- O(1) 
    - Move the bit to ith position and then do (|) with num's ith bit.
### Clear the i-th Bit
    return num & ~(1 << i)

    - Time:- O(1). Space:- O(1)
    - Move the bit to ith position and then do (&) with num's ith bit and (~ of 1).
### Toggle the i-th Bit
    return num ^ (1 << i)

    - Time:- O(1). Space:- O(1)
    - Move the bit to ith position and then do (^) with num's ith bit
---
### Set the rightmost UnSet Bit / Set the LAST 0 bit
    return n | (n + 1)

- Time:- O(1). Space:- O(1)
- (n + 1) flips the rightmost 0 in (n) to 1. 
- For example:- 
    - 6 -> 11**0** and 7 -> 11**1**.
    - 7 -> **0**111 and 8 -> **1**000. 
    - 8 -> 100**0** and 9 -> 100**1**.
    - 9 -> 10**0**1 and 10 -> 10**1**0.
- Performing OR, will Set the last 0 bit, while leaving other bits unchanged.
### Clear the rightmost Bit / UnSet the LAST 1 bit
    return n & (n - 1)

- Time:- O(1). Space:- O(1)
- (n - 1) flips the rightmost 1 in (n) to 0.
- For example:- 
    - 7 -> 11**1** and 6 -> 11**0**.
    - 8 -> **1**000 and 7 -> **0**111. 
    - 9 -> 100**1** and 8 -> 100**0**.
    - 10 -> 10**1**0 and 9 -> 10**0**1.
- Performing AND, will UnSet the last 1 bit, while leaving other bits unchanged.
### Detect if the number is a Power of TWO or not.
    if n<=0: return "No"
    if (n & n-1 == 0) return "Yes" else "No" 
    
- Time:- O(1). Space:- O(1)
- For example:- 
    2^4 -> 16 -> **1**0000
    2^5 -> 32 -> **1**00000 
- So we basically UnSet the rightmost bit and check if the number is 0 or not. 
- If it is 0, meaning the number is a power of 2 (2^3 -> 8 -> **1**000; 2^4 -> 16 -> **1**0000; 2^5 -> 32 -> **1**00000)
### Count number of Set-Bits
    count = 0
    while n>0:
        n = n & (n - 1)  # Turn off the rightmost set bit
        count += 1
    return count

- Time:- O(k) - number of set bits. Space:- O(1)
- Keep on doing this - **UnSet the LAST 1 bit**, untill n is not zero - return the count
- Here we keep on removing the rightmost bit one by one till n is not zero. This gives us count of all set bits
### Count number of SET-Bits (alternate approach)
    count = 0
    for i in range(32):
        count += (num & 1)
        num = num >> 1 # Shift the number every time by 1 place    
    return count

- Time:- O(k) - number of set bits. Space:- O(1)
- Here we move the number by 32 bits (since INTEGER number is of max 32 bits).
- While moving we AND with 1. While doing AND. if the current bit of n is 1 then the result becomes 1 else 0.
- so we count the number of times  (n & 1) gives 1. then return count
---
### Check if ODD or EVEN
    if (n & 1 == 0): "Even" 
    else: "Odd"

- Time:- O(1). Space:- O(1)
- If a number is odd its last bit is always 1. (e.g - 3,5,7,9)
- So We check if the last bit is 1, then it is odd. if it is 0, then it is even
### Swapping Two Numbers Without a Third Variable
    def fun(self, A,B):
        A = A^B
        B = A^B
        A = A^B
        return A,B
    
- Time:- O(1). Space:- O(1)

<br>

# Problems

## 1. Min bits required to flip to reach target from start.
#### Code File: MinimumBitFlipstoConvertNumber.py
#### Question:- Given two integers start and goal. Flip the minimum number of bits of start integer to convert it into goal integer.
#### Input:- start = 10 , goal = 7
#### Output:-  3
#### Explanation:-
> The binary representation of 10 is "**1****0**1**0**". The binary representation of 7 is "**0****1**1**1**". If we flip 3 bits of 10 then we get our goal(7).

> count bits that are different. (do xor)

> count set bits
#### Code:-
    def fun(self, start,goal):
        #get number of bits that differ
        val = start ^ goal 
        #count number of set bits
        c=0
        while val>0:
            val = val & (val-1)
            c=c+1
        return c
#### Complexity:-
- Time:- O(1) 
- Space:- O(1)

## 2. Single Number 1.
#### Code File: SingleNumber-1.py
#### Question:- Given an array - every element appears twice except for one. Find that single one..
#### Input:- num=[2,2,1]
#### Output:-  1
#### Explanation:-
> XOR of two same values gives you 0 and two diff values gives 1

> So XOR all elements inside the arr - the duplicates will be 0 and only the unique element remains 
#### Code:-
    def fun(self, nums):
        res=0
        for n in nums:
            res = res^n
        return res
#### Complexity:-
- Time:- O(N) 
- Space:- O(1)

## 3. Single Number 3.
#### Code File: SingleNumber-3.py
#### Question:- Given an array - every element appears twice except for two integers. Find those two single one integers
#### Input:- num=[1, 2, 1, 3, 5, 2]
#### Output:- [3, 5]
#### Explanation:-
>  Use 2 buckets and based on rightmost set bit we divided all numbers into those 2 buckets and then do XOR within those two buckets separately

>  **see code file for detailed explanation..**
#### Code:-
    def fun(self, nums):
        res=0
        for n in nums:
            res=res^n
        rightmost = (res & res-1) ^ res
        b1=0
        b2=0
        for n in nums:
            if n & rightmost !=0 : b1=b1^n
            else: b2=b2^n
        return [b1,b2]
#### Complexity:-
- Time:- O(N) 
- Space:- O(1)
 
## 3. Subsets-1 / PowerSet.
#### Code File: Subsets.py
#### Question:- Given an array of numbers, print all subsets of it using bitwise operators.
#### Input:- nums = [1, 2, 3]
#### Output:- [[ ], [1], [2], [3], [1, 2], [2, 3], [3, 1], [1, 2, 3]]
#### Explanation:-
> We can do this using recurion. and also using bitmanipulation

> Using bit, we generate all the numbers from (0 -> 2^n-1). For e.g. n=3, so 0->7.

> We choose those numbers from array [1,2,3] whos corresponding bits are set -> 000, 001, 010, 011, 100, 101, 110, 111.
#### Code:-
    # 2**n => 1<<n -> Optimization
    # convert val to bits
    # count set bits (i)
    # put nums[i] in curr
    # finally put curr in res
    
    for val in range(1<<n):
        curr=[]
        for i in range(n):
            if((1<<i) & val):
                curr.append(nums[i])
        res.append(curr)
    return res
#### Complexity:-
- Time:- O(N x 2N) - 2^N combinations. N is the number of elements in the input array.
- Space:- O(N x 2N) - 2^N combinations, each subset can have at most N elements.

## 4. XOR Of numbers from L to R. (Trick - byheart)
#### Code File: XOROfNumbersFromLToR.py
#### Question:- Given two integers L and R. Find the XOR of the elements in the range [L , R].
#### Input:- L = 3 , R = 5
#### Output:- 2
#### Explanation:-
> we can do XOR of all elements from L to R, and return. But the time complexity would be O(n). We want it to be in O(1) 

> This code is pretty much by-heart. no tricks just pattern to observe on n%4.

> to get XOR from L to R -> apply XOR from -> (1 -> R) and (1 -> L-1)

> doing this we eliminate the common elements from (1 -> L-1) and keep only elements from (L to R)

> To find XOR from 1 to n (n could be L-1 or R) - we use the below logic

    n%4==1: return 1
    n%4==2: return n+1
    n%4==3: return 0
    n%4==0: return n
#### Code:-
    # func to find xor from 1 to n
    def help(self,n):
        if n%4==1: return 1
        elif n%4==2: return n+1
        elif n%4==3: return 0
        elif n%4==0: return n
    def fun(self, L, R):
        return help(L-1) ^ self.help(R)
#### Complexity:-
- Time:- O(1)
- Space:- O(1)


## 5. Divide 2 numbers without multiplication of division
#### Code File: DivideTwoNumbersWithoutMultiplicationOrDivision.py
#### Question:- Given dividend and divisor. Divide without using the mod, division, or multiplication operators and return the quotient.
#### Input:- Dividend = 22, Divisor = 3
#### Output:- 3
#### Explanation:- See the code file for full explanation
> the brute force is - keep on removing divisor from dividend - untill dividend is less than divisor. 

> If divisor is 1 and dividend is 2**31-1. Then it will lead to time limit exceed.

> Remove the largest possible value (multiple of divisor) from the dividend first, 
    then remove the second-largest value (multiple of divisor) from the dividend,
    then remove 3rd largest ..and so on!! - untill dividend is less than divisor.

> Remove 12(3 x 2^2) from 22, left with 10. 

> remove 6(3 x 2^1), left with 4. 

> remove 3(3 x 2^0), left with 1. stop. 

> Sum (2^2 + 2^1 + 2^0) = 7. return
#### Code:-
    See the code file
#### Complexity:-
- See the code file

<br>

# AdvanceMath
## 1. Print Prime **Factorization** of a number
#### Code File: PrintPrimeFactorizationOfANumber.py
#### Question:- Given a number - return prime factorization of that number. e.g -  780 -> [2, 2, 3, 5, 13]
#### Input:- [7, 12, 18, 780]
#### Output:- [[7], [2, 2, 3], [2, 3, 3], [2, 2, 3, 5, 13]]
#### Explanation:-
> the brute force is - start i from 2 till num. start dividing the num with i

> while num%i==0 -> num = num/i and curr.append(i)

> at the end of the for loop return curr

> we can optimize this where we only travel from 2 till sqrt(num). 

> At the end if num is still not 1 then curr.append(num). 

> ensuring that we add the last prime number which divides the item completely (see striver video for this)
#### Code:-
    def getPrimeFactorization(self, item):
        curr=[]
        for p in range(2, int(math.sqrt(item))+1):
            while item % p == 0:
                item = item / p 
                curr.append(p)
        if item!=1: curr.append(int(item))
        return curr

    res=[]
    for item in q:
        res.append(self.getPrimeFactorization(item))
    return res
#### Complexity:-
- time:-O(sqrt(item) * logn) * O(N) -> N is size of queries, O(sqrt(item)) is the (2->sqrt(item)+1) loop. and logn for the inner while loop
- space:-O(log(item)) list stores the prime factors. The number of prime factors for any number log(number)

## 2. Print Prime **Factors** of a number
#### Code File: PrintPrimeFactorsOfANumber.py
#### Question:- Given a number - return prime factors of that number. e.g -  780 -> [2, 3, 5, 13]
#### Input:- [7, 12, 18, 780]
#### Output:- [[7], [2, 3], [2, 3], [2, 3, 5, 13]]
#### Explanation:-
> much similar to the above one. Only dfference is that we need unique factors. So the code changes slitely
#### Code:-
    for p in range(2, int(math.sqrt(item))+1):
        if item % p == 0:
            curr.append(p)
            while item % p == 0:
                item = item / p
    if item!=1: curr.append(int(item))
    return curr
#### Complexity:-
- time:-O(sqrt(item) * logn) * O(N) -> N is size of queries, O(sqrt(item)) is the (2->sqrt(item)+1) loop. and logn for the inner while loop
- space:-O(log(item)) list stores the prime factors. The number of prime factors for any number log(number)

## 3. Print all Divisors of a number
#### Code File: Print all DivisorsOfANumber.py
#### Question:- Given an integer N, return all divisors of N.
#### Input:- N = 36
#### Output:- [1, 2, 3, 4, 6, 9, 12, 18, 36]
#### Explanation:-
> go from 1 to n, if i divides n then add i to curr. return curr

> optimization - similar to the above - we could just go till sqrt(n). 

> if i divides n. add i. and also add n//i. this ensures that we are adding i and also its multiples (n//i)

> while doing that check if we not add duplicate . e.g. 6,6 -> 36
#### Code:-
    for p in range(1, int(math.sqrt(item))+1):
            if item % p == 0: 
                curr.append(p)
                if item//p != p: #to get rid of duplicate 6.
                    curr.append(item//p)
    return curr
#### Complexity:-
- time:- O(sqrt(n)) - loop till sqrt(n)
- space:- O(2*sqrt(N)) - curr stores all items from 1 till (2 x sqrt(n))

## 4. Count Primes 
- Sieve of Eratosthenes - see solution and striver video

## 5. Pow(x,n)
#### Code File: Pow.py
#### Question:-  Implement the power function pow(x, n) , which calculates the x raised to n i.e. x^n.
#### Input:- x = 2.0000, n = 10
#### Output:- 1024.0000 
#### Explanation:-
> so there are 2 parts. if n is even and n is odd

> if n is even - recursively calculate the power by squaring the base and halving the exponent. 

> power(x, n) = power(x * x, n / 2)

> if n is odd - recursively calculate the power by multiplying the base with the result of the power function for n - 1. 

> power(x, n) = x * power(x, n - 1)

> finally if n<0 - take the reciprocal of the result.
#### Code:-
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
#### Complexity:-
- time:- O(log(n))
- space:- O(log(n))

<br>

# Summary
### Bit manipulation tricks
- Check if the i-th Bit is Set
- Set the i-th Bit
- Clear the i-th Bit
- Toggle the i-th Bit
---
- Set the rightmost Bit
- Clear the rightmost Bit
- Detect if the number is Power of TWO.
- Count number of SET-Bits
---
- detect even or odd
- Swapping of 2 numbers
### Problems
- Min bits required to flip to reach target from start
- Single number 1
- Single number 3 (Trick - 2 buckets)
- Subset-1
- Divide 2 numbers without multiplication of division (Trick - divide the largest number first)
- XOR Of numbers from L to R. (Trick)
### Math
- Print Prime **Factorization**
- Print Prime **Factors**
- Print all Divisors
- Count Primes (Trick - HARD)
- Pow(x,n) (Trick - even/odd)
---
---
### DSA Sheet Questions included
- Single number 1
- Divide Two Integers
- Count Primes (Math)
- Pow(x,n) (Math)
### DSA Sheet Questions NOT included
- Add Binary
- Reverse Bits
- Number of 1 Bits
- Single Number II
- Bitwise AND of Numbers Range
- Counting Bits
- Palindrome Number (Math)
- Plus One (Math)
- Factorial Trailing Zeroes (Math)
- Sqrt(x) (Math)
- Max Points on a Line (Math)
- Fizz Buzz (Math)
- Power of Three (Math)
- Excel Sheet Column Number (Math)
- Fraction to Recurring Decimal (Math)
- Largest Number (Math)
- Max Points on a Line (Math)
- Multiply Strings (Math)
- Detect Squares (Math)