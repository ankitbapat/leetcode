from queue import Queue
class StackUsingQueue():
    def __init__(self, size=1000):
        self.queue = Queue()
        
    def push(self, item):
        s = self.queue.qsize() #current no of elements in queue
        self.queue.put(item)
        for _ in range(s): # avoid the recent inserted element, take the rest
            self.queue.put(self.queue.get())
    
    def pop(self):
        n = self.queue.queue[0]
        self.queue.get() # removed element
        return n
    
    def top(self):
        return self.queue.queue[0]
    
    def isEmpty(self):
        return self.queue.empty()

class Solution():
    def fun(self, instr, values):
        for i in range(len(instr)):
            if instr[i]=="QueueStack":
                qs = StackUsingQueue()
                print("null", end=" ")
            elif instr[i]=="push":
                qs.push(values[i][0])
                print("null", end=" ")
            elif instr[i]=="pop":
                print(qs.pop(), end=" ")
            elif instr[i]=="top":
                print(qs.top(), end=" ")
            elif instr[i]=="isEmpty":
                print(qs.isEmpty(), end=" ")
sol=Solution()
instr = ["QueueStack", "push", "push", "pop", "top", "isEmpty"]  
values = [[], [4], [8], [], [], []]  
sol.fun(instr, values)

# Time:- Push O(n). Rest all O(1)
# Space:- O(n)