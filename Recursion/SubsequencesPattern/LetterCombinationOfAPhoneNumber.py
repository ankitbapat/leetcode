class Solution:
    def fun(self, d_index, curr, res, digits, map_digits):
        if d_index==len(digits):
            res.append(curr)
            return
        
        st = map_digits[digits[d_index]]
        for i in range(len(st)):
            # curr.append(st[i])
            self.fun(d_index+1, curr+st[i], res, digits, map_digits)
            # curr.pop()
        
s=Solution()
res=[]
digits = "23"
map_digits = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}
s.fun(0, "", res, digits, map_digits)
print(res)

# Time:- O(N^D) * N - number of digits (D). length of string(abc,def,etc..) (N). multiplied by N coz concatenating each string takes N time
#   For example:- 3 places 2 choises to make at each place. complexity is "2^3". total 8 choices

# Space:- O(D) - stack space depth (number of digits (D))
# Space complexity could also be O(N^D)*O(N) because N^D * N are the total combinations that gets generated.
# But we take stack-space into consideration instead of space required to store the result

# So Space including output:- results space
# space without including output:- stack space