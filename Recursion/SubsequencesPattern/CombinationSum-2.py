class Solution:
    def fun(self, nums, target, index, curr, res):
        if target==0:
            res.append(curr.copy())
            return
        for i in range(index,len(nums)):
            if target<nums[i]:break
            if i > index and nums[i]==nums[i-1]: continue
            curr.append(nums[i])
            self.fun(nums, target-nums[i], i+1, curr, res)
            curr.pop()
s=Solution()
nums = [10,1,2,7,6,1,5] # [1,1,2,5,6,7,10]
nums1 = [1,1,1,2,2]
target = 8
res=[]
nums=sorted(nums)
s.fun(nums, target, 0, [], res)
print(res)

# time:- 2^n * K
# space:- O(k * X) -> the space complexity is variable and dependents on number of combinations generated (X). k-> size of curr. 
# k (size of curr) * X (number of curr)
