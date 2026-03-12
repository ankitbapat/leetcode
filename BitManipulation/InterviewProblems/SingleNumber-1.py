class Solution():
    def fun(self, nums):
        res=0
        for n in nums:
            res = res^n
        return res
    
sol=Solution()
nums=[2,2,1]
# nums=[4,1,2,1,2]
print(sol.fun(nums))

# Time: O(N). Where N is the size of the array
# Space: O(1). No extra space used