
# Get all subsequence with sum k
class Solution:
    def fun(self, index, curr, nums, sum, k, res):
        if index==len(nums):
            if sum==k:
                res.append(curr.copy())
            return
        
        curr.append(nums[index])
        sum=sum+nums[index]
        self.fun(index+1, curr, nums, sum, k, res)
        curr.pop()
        sum=sum-nums[index]
        self.fun(index+1, curr, nums, sum, k, res)

s=Solution()
nums = [4, 9, 2, 5, 1]
k = 10
res=[]
s.fun(0, [], nums, 0, k, res)
print(res)

# Count all subsequence with sum k
class Solution:
    def fun(self, index, nums, sum, k):
        if index==len(nums):
            if sum==k:
                return 1
            return 0
        
        sum=sum+nums[index]
        l = self.fun(index+1, nums, sum, k)
        sum=sum-nums[index]
        r = self.fun(index+1, nums, sum, k)
        return l+r

s=Solution()
nums = [4, 9, 2, 5, 1]
k = 10
print(s.fun(0, nums, 0, k))

# Time:-O(2^n) - Each element has 2 choices - choose/not-choose
# Space:-O(n) - Stack size