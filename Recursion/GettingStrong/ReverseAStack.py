class Solution():
    def insert_at_last(self, stack, temp):
        if not stack:
            stack.append(temp)
            return
        
        val = stack.pop()
        self.insert_at_last(stack, temp)
        stack.append(val)

    def reverseStack(self, stack):
        if stack:
            temp = stack.pop()
            self.reverseStack(stack)
            self.insert_at_last(stack, temp)

sol=Solution()
stack = [4, 1, 3, 2]
sol.reverseStack(stack)
print(stack)

# Time:- O(n^2)
# Space:-O(n)