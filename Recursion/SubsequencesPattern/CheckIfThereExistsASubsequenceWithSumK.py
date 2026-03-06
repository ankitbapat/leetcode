class Solution:
    def fun(self, index, nums, k, sum):
        if index==len(nums):
            if sum==k:
                return True
            return False

        sum=sum+nums[index]
        if self.fun(index+1, nums, k, sum) : return True
        sum=sum-nums[index]
        if self.fun(index+1, nums, k, sum) : return True
        return False

s=Solution()
nums = [4, 9, 2, 5, 1]
k = 10
print(s.fun(0, nums, k, 0))