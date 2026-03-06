class Solution():
    def isPalindrome(self, s):
        return s==s[::-1]
    
    def fun(self, s, index, curr, res):
        if index==len(s):
            res.append(curr.copy())
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s[index:i+1]):
                curr.append(s[index:i+1])
                self.fun(s, i+1, curr, res)
                curr.pop()
        


sol=Solution()
res=[]
s="aabb"
sol.fun(s, 0, [], res)
print(res)

# time:O(2^len(s) * s) -> 2^len(s) at each step we decide weather to pick or not pick a character. Also for calculating palindrome we need O(len(s))
# space:- O(len(s)) -> stack depth