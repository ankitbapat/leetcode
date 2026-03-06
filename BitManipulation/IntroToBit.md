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

# Right Shift (>>): Shifts bits to the right, fills left with 0s.
# 13 >> 1 = 0110 → 6

# Left Shift (<<): Shifts bits to the left, fills right with 0s.
# 13 << 1 = 11010 → 26

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