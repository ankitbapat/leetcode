# Print all the combinations. This is similar to power set or print all subsequence - choose 1 or 0.
class solution:
    def fun(self, n, curr):
        if len(curr) == n: 
            res.append(curr)
            return

        self.fun(n, curr+"0")
        self.fun(n, curr+"1")
        

s=solution()
n=3
res=[]
curr=""
s.fun(n, curr)
print(res)

# POWER SET
# Print All Subsequences / Power Set
# Using Recursion - choose/not-choose
# video:- https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6
class solution:
    def fun(self, index, curr, arr, res):
        if index>=len(arr):
            res.append(curr.copy()) #thing to remember
            return
        curr.append(arr[index])
        self.fun(index+1, curr, arr, res)
        curr.pop()
        self.fun(index+1, curr, arr, res)

s=solution()
arr=[3, 1, 2]
res=[]
curr=[]
s.fun(0, curr, arr, res)
print(res)

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

# Count all subsequence with sum k (l/r)
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

# Check if there exsists a subsequence with sum k (True/False)
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


# Time:-O(2^n) - Each element has 2 choices - choose/not-choose
# Space:-O(n) - Stack size


#Pattern:-
Generate PowerSet/Subsequence :- (pick/no-pick) 
    Count powerset/subsequence with sum=k :- (return 1/0) 
    Check if powerset/subsequence exists with sum=k :- (return T/F)
CombinationSum-1 (Can take one item infinite time):- pick/no-pick with if condition
CombinationSum-2 (Duplicates):- pick using a for loop
SubsetSum-1 (Print sum of subsequences):- pick/no-pick
SubsetSum-2 (Duplicates):- 
