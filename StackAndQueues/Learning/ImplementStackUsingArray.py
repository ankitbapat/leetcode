class Stack:
    def __init__ (self, size=1000):
        self.arr = [0] * size
        self.capacity = size
        self.topIndex = -1

    def push(self, item):
        if self.topIndex > self.capacity:
            print("stack overflow")
            return
        self.topIndex = self.topIndex + 1
        self.arr[self.topIndex] = item

    def pop(self):
        if self.topIndex < 0:
            print("stack already empty")
            return
        val = self.arr[self.topIndex]
        self.topIndex = self.topIndex - 1
        return val
    
    def top(self):
        if self.topIndex < 0:
            print("stack already empty")
            return -1
        return self.arr[self.topIndex]
    
    def isEmpty(self):
        return "True" if len(self.arr) == 0 else "False"

class Solution:
    def fun(self, instr, values):
        for i in range(len(instr)):
            if instr[i] == "ArrayStack":
                st = Stack(1000)
                print("null", end=" ") 
            elif instr[i] == "push":
                st.push(values[i][0]) 
                print("null", end=" ")
            elif instr[i] == "pop":
                print( st.pop(), end=" ")
            elif instr[i] == "top":
                print( st.top(), end=" ")
            elif instr[i] == "isEmpty":
                print(st.isEmpty()) 
                
sol=Solution()
instr = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]  
values = [[], [5], [10], [], [], []]  
sol.fun(instr, values)

# time:- O(1) for all operations (push, pop, top, isEmpty).
# space:- O(n)