class Solution():
    def insert(self, stack, temp):
        if not stack or stack[-1] <= temp:
            stack.append(temp)
            return
        
        val = stack.pop()
        self.insert(stack, temp)
        stack.append(val)

    def sortStack(self, stack):
        if stack:
            temp = stack.pop()
            self.sortStack(stack)
            self.insert(stack, temp)

sol=Solution()
stack = [4, 1, 3, 2]
sol.sortStack(stack)
print(stack)

# Time:- O(n^2)
# Space:-O(n)