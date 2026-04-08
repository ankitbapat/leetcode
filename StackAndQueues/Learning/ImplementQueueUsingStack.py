
class QueueUsingStack:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    
    def push(self, item):
        while len(self.stack_1) > 0:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(item)
        while len(self.stack_2) > 0:
            self.stack_1.append(self.stack_2.pop())
    
    def pop(self):
        if len(self.stack_1) == 0: 
            print("Empty")
            return -1
        return self.stack_1.pop()
    
    def peek(self):
        if len(self.stack_1) == 0: 
            print("Empty")
            return -1
        return self.stack_1[-1]
    
    def isEmpty(self):
        return len(self.stack_1) == 0

# time:- O(n) for push rest O(1)
# space:- O(n)


# Optimal Approach:-
# when push() is O(1) and pop & peek is O(n)
# why this is optimal because pop & peek O(n) happens rearly. 
# On the other hand the above solution is brute because for push everytime it will be O(n)
class QueueUsingStack_Push_O1:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    
    def push(self, item):
        self.stack_1.append(item)
    
    def pop(self):
        if len(self.stack_2) == 0: # this is important because, if stack_2 is full, it should not get items from stack_1. instead just return the top element for itself
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        
        if len(self.stack_2) == 0: # even after the transfer the elements are not present in stack_2, then it is empty queue
            print("Empty")
            return -1
        
        return self.stack_2.pop()
    
    def peek(self):
        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        
        if len(self.stack_2) == 0: 
            print("Empty")
            return -1
        
        return self.stack_2[-1]
    
    def isEmpty(self):
        return len(self.stack_1) == 0 and len(self.stack_2) == 0 # here we check both the stacks, since we could have elements in both

# time:- O(1) for push and O(n) for pop and peek but in worst case
# space:- O(n)

class Solution:
    def fun(self, instr, items):
        for i in range(len(instr)):
            if instr[i] == "StackQueue":
                queue = QueueUsingStack()
                print("null", end=" ") 
            elif instr[i] == "push":
                queue.push(items[i][0])
                print("null", end=" ") 
            elif instr[i] == "pop":
                print(queue.pop(), end=" ")
            elif instr[i] == "peek":
                print(queue.peek(), end=" ")
            elif instr[i] == "isEmpty":
                print(queue.isEmpty(), end=" ")
    
    def fun_push_O1(self, instr, items):
        for i in range(len(instr)):
            if instr[i] == "StackQueue":
                queue = QueueUsingStack_Push_O1()
                print("null", end=" ") 
            elif instr[i] == "push":
                queue.push(items[i][0])
                print("null", end=" ") 
            elif instr[i] == "pop":
                print(queue.pop(), end=" ")
            elif instr[i] == "peek":
                print(queue.peek(), end=" ")
            elif instr[i] == "isEmpty":
                print(queue.isEmpty(), end=" ")

sol=Solution()
instr = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]  
items = [[], [4], [8], [], [], []]   
sol.fun(instr, items)
print() #break line
sol.fun_push_O1(instr, items)



