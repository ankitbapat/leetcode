class StackUsingArray:
    def __init__ (self, size=1000):
        self.arr = [0] * size
        self.capacity = size
        self.topIndex = -1

    def push(self, item):
        if self.topIndex == self.capacity - 1:
            print("stack overflow")
            return
        self.topIndex = self.topIndex + 1
        self.arr[self.topIndex] = item

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        val = self.arr[self.topIndex]
        self.topIndex = self.topIndex - 1
        return val
    
    def top(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        return self.arr[self.topIndex]
    
    def isEmpty(self):
        return self.topIndex == -1

class Solution:
    def fun(self, instr, values):
        for i in range(len(instr)):
            if instr[i] == "ArrayStack":
                st = StackUsingArray(1000)
                print("null", end=" ") 
            elif instr[i] == "push":
                st.push(values[i][0]) 
                print("null", end=" ")
            elif instr[i] == "pop":
                print( st.pop(), end=" ")
            elif instr[i] == "top":
                print( st.top(), end=" ")
            elif instr[i] == "isEmpty":
                print(st.isEmpty(), end=" ") 
                
sol=Solution()
instr = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]  
values = [[], [5], [10], [], [], []]  
sol.fun(instr, values)

# time:- O(1) for all operations (push, pop, top, isEmpty).
# space:- O(n)