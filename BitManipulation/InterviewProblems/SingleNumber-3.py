#brute force
class Solution():
    def fun(self, nums):
        obj={}
        for n in nums:
            if n not in obj: obj[n]=1
            else: obj[n]=obj[n]+1
        return set(obj.values())
       

sol=Solution()
nums=[1, 2, 1, 3, 5, 2]
print(sol.fun(nums))

# Time: O(n)
# Space: O(n)

#optimal
# logic:-
#  xor all numbers.
#  the 2 numbers will get XORed. -> lets call this number XORed number (3^5)
# the two numbers which are different - they have ATLEAST one ( OR MORE than one) bits that are different.
# the set bits(1) of the XORed number represent that those bits are different in 3 and 5.
# We have to find only one bit (lets say the rightmost bit) which is SET(1) in this XORed number.
    # Why? becasue this bit is different in both the numbers 3 and 5. 
    # We can then put all the numbers into 2 different buckets based on that rightmost set bit.
    # This will guarantee that 3 will be in 1st bucket and 5 withh be in 2nd bucket. so we separated those two numbers

class Solution():
    def fun(self, nums):
        res=0
        for n in nums:
            res=res^n
        #find the rightmost set bit:- 
        #   how to do that. 
        #   we can only set the rightmost bit (n = n | n+1) or unset it(n = n & n-1). 
        #   so what we did is that - 
        #       we unset the rightmost most bit (n & n-1)
        #       we then XOr that with the original number. 
        #            why?- because that rightmost bit which was unset is the only bit that is changed (from 1 to -> 0).
        #            So XOR of that number with itself will have all bits as zero, except that rightmost bit. 
        #            so we get something like this:- ...0000001000000.. 
        rightmost = (res & res-1) ^ res
        
        # now we use this 2 different buckets and we put each item into it.
        #   If the & operation between n and rightmost bit is not equal to 0. (meaning - that bit is SET in that number)
        #   Else (meaning - that bit is UNSET in that number)
        
        #   in the if and else condition we keep on doing XOR for all the elements 
        #   so the duplicates will be gone and only 3 remains in 1st bucket and 5 remains in the 2nd bucket
        b1=0
        b2=0
        for n in nums:
            if n & rightmost !=0 : b1=b1^n
            else: b2=b2^n
        return [b1,b2]
       

sol=Solution()
nums=[1, 2, 1, 3, 5, 2]
print(sol.fun(nums))

# Time: O(n)
# Space: O(2) -> O(1) -> 2 bits to be stored in res array