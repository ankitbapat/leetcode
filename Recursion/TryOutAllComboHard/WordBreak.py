class Solution():
    def fun(self,i):
        if i==len(s): return True
        for w in wordDict:
            if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                if self.fun(i+len(w)): 
                    return True
        return False

       

sol=Solution()
# s = "takeuforward"
# wordDict = ["take" , "forward" , "you", "u"]
# s = "leetcode" 
# wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
s = "aaaaaaa"
wordDict = ["aaa", "aaaa"]
print(sol.fun(0))

# time:- W are the words and S is the length of string. At each character we can make W choices. so O(W^S). 
# Now length of longest word in dict is L. So to check a word of length L at each step (position), 
# the total complexity is O(L* W^S)
# space:- Recursion depth - O(S)