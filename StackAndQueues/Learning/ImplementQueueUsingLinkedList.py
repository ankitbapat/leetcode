class Node:
    def __init__ (self, val=-1, next=None):
        self.val = val
        self.next = next

class QueueUsingLinkedList:
    def __init__(self):
        self.start = self.end = None
        self.size=0

    def push(self, item):
        node = Node(item)
        if self.start is None:
            self.start = self.end = node
        else:
            self.end.next = node
            self.end = node
        self.size += 1

    def pop(self):
        if self.start is None: 
            return -1
        val = self.start.val
        temp = self.start
        self.start = self.start.next

        # FIX: when we pop the last item. start=None. So, we have point end to None too!
        if self.start is None: self.end = None

        del temp
        self.size -= 1
        return val
    
    def peek(self):
        if self.start is None: return -1
        return self.start.val
    
    def isEmpty(self):
        return self.size == 0
    
class Solution:
    def fun(self, instr, values):
        for i in range(len(instr)):
            if instr[i] == "LinkedListQueue":
                st = QueueUsingLinkedList()
                print("null", end=" ") 
            elif instr[i] == "push":
                st.push(values[i][0]) 
                print("null", end=" ")
            elif instr[i] == "pop":
                print( st.pop(), end=" ")
            elif instr[i] == "peek":
                print( st.peek(), end=" ")
            elif instr[i] == "isEmpty":
                print(st.isEmpty(), end=" ") 
                
sol=Solution()
instr = ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"] 
values = [[], [3], [7], [], [], []]     
sol.fun(instr, values)

# time:- O(1)
# space: O(n)