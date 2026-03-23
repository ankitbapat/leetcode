class Solution:
    def fun(self, nums, index, sum, res):
        if len(nums)==index:
            res.append(sum)
            return
        self.fun(nums, index+1, sum+nums[index], res)
        self.fun(nums, index+1, sum, res)

s=Solution()
nums = [5,2,1]
res=[]
s.fun(nums, 0, 0, res)
res.sort()
print(res)

# Time:- O(2^n * log(2^n)) - 2^n coz of generating subsets (pick/no-pick) and log(2^n) is for sorting
# space:- O(2^n + n) - The result array holds all subset sums, requiring O(2n) space. Recursion uses an additional O(n) stack space. so total - O(2^n + n).