# Decimal to Binary
# 13 -> 1101 divide the number repeatably by 2 till quotient reaches 1. 
# 13 / 2 = 6 remainder 1
# 6 / 2 = 3 remainder 0
# 3 / 2 = 1 remainder 1
# 1 / 2 = 0 remainder 1

# Binary to Decimal
# Each bit is multiplied by 2 raised to the power of its position index. 
# 1 * 2^0 = 1
# 0 * 2^1 = 0
# 1 * 2^2 = 4
# 1 * 2^3 = 8
# 1011 -> 8+2+1 (13)

# One's complement
# Binary of 13     : 0000 1101
# One's Complement : 1111 0010

# Two's complement:- We take the 2's complement of a binary number primarily to represent signed negative numbers
# One's Complement : 1111 0010
# Add 1            : 1111 0011

# AND (&)
# 13: 1101
#  7: 0111
# &  : 0101 → 5

# OR (|)
# 13: 1101
#  7: 0111
# |  : 1111 → 15

# XOR (^) :- If bits differ, the result is 1; if the same, result is 0.
# 13: 1101
#  7: 0111
# ^  : 1010 → 10

# NOT (~)
# 5: 0000 0101
# ~5: 1111 1010 → -6 (in two's complement)

# Right Shift (>>): Shifts bits to the right by 1 position, fills left with 0s.
# 13(1101) >> 1 => 1101 >> 1 => 0110 → 6

# Left Shift (<<): Shifts bits to the left by 1 position, fills right with 0s.
# 13(1101) << 1 => 1101 << 1 => 11010 → 26

# Tricks:-
# 1. Swapping Two Numbers Without a Third Variable
# A = A^B
# B = A^B
# A = A^B

# 2. Checking if the i-th Bit is Set
# (1 << i) & num   → if res==0 then unset, else set
# - move the bit to ith position and then do (&) with num's ith bit.

# 3. Setting the i-th Bit
# num | (1 << i). 
# - move the bit to ith position and then do (|) with num's ith bit.

# 4. Clearing the i-th Bit
# num & ~(1 << i)
# - move the bit to ith position and then do (&) with num's ith bit and (~ of 1).

# 5. Toggling the i-th Bit
# num ^ (1 << i)
# - move the bit to ith position and then do (^) with num's ith bit

# 6.  Count number of all Set bits / Remove the rightmost bit - brian Kernighan's algo
# while num>0:
#    num = num & (num-1)
#    count=count+1
# return count
# Here we keep on removing the rightmost or the smallest bit one by one till n is not zero.
# This gives us count of all set bits

# 7. Set the rightmost bit to 1.
#    return (n | n+1)
#    n + 1 flips the rightmost 0 in n to 1, 
#    Performing OR sets that bit to 1 while leaving other bits unchanged.

# 8. Check ODD or EVEN
# if (n & 1 == 0): "Even" 
# else: "Odd"

# 8. detect if the number is a Power of two (n=2^x) => 2^4 -> 16 -> 10000; 2^5 - 32 -> 100000 
# if (n & n-1 == 0) return "Yes" else "No" 

# 9. UNSET rightmost bit:-
# n = n & (n - 1)

# 10. SET rightmost bit:-
# n = n | (n + 1)

# 11. Count number of SET-bits
# count = 0
# while n>0:
#    n = n & (n - 1)  # Turn off the rightmost set bit
#    count += 1
# return count

# 12. Count number of SET-bits (alternate approach)
# count = 0
# for i in range(32):
#     count += (num & 1)
#     num = num >> 1 # Shift the number every time by 1 place    
# return count

