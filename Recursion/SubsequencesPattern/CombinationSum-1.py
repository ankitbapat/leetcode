class Solution:
    def fun(self, nums, target, index, curr, res):

        if index==len(nums):
            if target==0:
                res.append(curr.copy())
            return

        if target>=nums[index]:
            curr.append(nums[index])
            self.fun(nums, target-nums[index], index, curr, res)
            curr.pop()
        self.fun(nums, target, index+1, curr, res)
       

s=Solution()
nums = [2,3,6,7]
target = 7
res=[]
s.fun(nums, target, 0, [], res)
print(res)

# time:- O(2^T) * K -> 2^T meaning - 2 to the power target(T). Why coz you keep on picking and non-picking till the target reduces to 0.
# Assume your nums=[1] and Target is 10. The complexity of pick/not-pick will be 2^T. We can pick/not-pick T times. K length of curr to copy
# space:- O(k * X) -> the space complexity is variable and dependents on number of combinations generated (X). k-> size of curr. 
# k (size of curr) * X (number of curr)