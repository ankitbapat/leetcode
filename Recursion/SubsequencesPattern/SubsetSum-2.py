class Solution:
    def fun(self, nums, index, curr, res):
        res.append(curr.copy())

        for i in range(index, len(nums)):
            if i>index and nums[i]==nums[i-1]: continue
            curr.append(nums[i])
            self.fun(nums, i+1, curr, res)
            curr.pop()

s=Solution()
nums = [1,2,2]
nums.sort()
res=[]
s.fun(nums, 0, [], res)
print(res)

# Time:- 2^n - for no. of combinations
# space:- 2^n - for no. of combinatinations to be stored + O(n) stack space