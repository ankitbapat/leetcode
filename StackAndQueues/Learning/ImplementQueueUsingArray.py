class QueueUsingArray:
    def __init__(self, size=1000):
        self.arr = [0] * size
        self.back = 0
        self.front = 0
        self.capacity = size
        self.size = 0
    
    def push(self, item):
        if self.size == self.capacity:
            print("queue overflow")
            return
        self.arr[self.back] = item
        self.back = (self.back + 1) % self.capacity # Wrap around using modulo
        self.size = self.size + 1
        
    def pop(self):
        if self.isEmpty():
            print("queue is empty")
            return -1
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity # Wrap around using modulo
        self.size = self.size - 1
        return val
    
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return -1
        return self.arr[self.front]
    
    def isEmpty(self):
        return self.size == 0
    
class solution:
    def fun(self, instr, items):
        for i in range(len(instr)):
            if instr[i] == "ArrayQueue":
                queue = QueueUsingArray(1000)
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

sol=solution()
instr = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]  
items = [[], [5], [10], [], [], []]  
sol.fun(instr, items)

# time:- O(1) for all operations (push, pop, top, isEmpty).
# space:- O(n)