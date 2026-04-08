
class MinStack:
    def __init__(self):
        self.st = []
        self.min_st = []
    
    def push(self, item):
        self.st.append(item)
        if self.min_st:
            m = min(self.min_st[-1], item) #this keeps only min value in the stack
            self.min_st.append(m)
        else:
            self.min_st.append(item) 

    def pop(self):
        self.min_st.pop()
        self.st.pop()

    def top(self):
        return self.st[-1]
    
    def getMin(self):
        return self.min_st[-1]

class Solution:
    def fun(self, instr, items):
        for i in range(len(instr)):
            if instr[i]=="MinStack":
                minStack = MinStack()
                print("null", end=" ")
            elif instr[i]=="push":
                minStack.push(items[i][0])
                print("null", end=" ")
            elif instr[i]=="pop":
                print(minStack.pop(), end=" ")
            elif instr[i]=="top":
                print(minStack.top(), end=" ")
            elif instr[i]=="getMin":
                print(minStack.getMin(), end=" ")
            
sol=Solution()
instr = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]  
items = [ [], [-2], [0], [-3], [ ], [ ], [ ], [ ] ] 
sol.fun(instr, items)

# time:-O(1)
# space:-O(n)