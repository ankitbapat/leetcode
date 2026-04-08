class Node:
    def __init__ (self, val=-1, next=None):
        self.val = val
        self.next = next

class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def push(self, item):
        node = Node(item)
        if self.head is None:
            self.head =node
            self.tail = self.head
        else:
            self.head.next = node
            self.head = node

    def pop(self):
        if self.head is None: return -1
        val = self.tail.val
        temp = self.tail
        self.tail = self.tail.next
        del temp
        return val
    
    def peek(self):
        if self.head is None: return -1
        return self.tail.val
    
    def isEmpty(self):
        return self.tail == self.head == None
    
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