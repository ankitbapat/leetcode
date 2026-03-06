class Solution:
    def fun(self, nums, target, k, curr, sum, index, res):
        if sum==target and len(curr)==k:
            res.append(curr.copy())
            return
        
        for i in range(index, 10):
            if sum+nums[i]>target: break
            if i>index and nums[i]==nums[i-1]:continue
            curr.append(nums[i])
            self.fun(nums, target, k, curr, sum+nums[i], i+1, res)
            curr.pop()
        
s=Solution()
nums = [1,2,3,4,5,6,7,8,9]
k = 3
n = 9
res=[]
s.fun(nums, n, k, [], 0, 0, res)
print(res)

# Time:- O(2^9 * k):- 2^9 comniations at each step. Plus k to copy the curr of length k into result
# Space:- O(k) - The maximum depth of the recursion tree is k, as we are only looking for a combination of k numbers.