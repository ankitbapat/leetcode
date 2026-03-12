class Solution():
    def fun(self, nums):
        n=len(nums)
        res=[]
        
        # 2**n => 1<<n -> Optimization
        for val in range(1<<n):
            curr=[]
            # convert val to bits
            # count set bits (i)
            # put nums[i] in curr
            # finally put curr in res
            for i in range(n):
                if((1<<i) & val):
                    curr.append(nums[i])
            res.append(curr)

        return res
    
    
sol=Solution()
nums=[1,2,3]
print(sol.fun(nums))

# time:- O(2^n) * O(n):- 2^n combinations (0 to 7 in this case). each combo is iterated n times
# space: O(2^n) * O(n):- where N is the number of elements in the input array. 
# We store all subsets in a list. Since there are 2N subsets in the power set, each subset can have at most N elements.
