class Node:
    def __init__ (self, val=-1, next=None):
        self.val = val
        self.next = next

class StackUsingLinkedList:
    def __init__ (self):
        self.head = None

    def push(self, item): # we build LL backwards
        node = Node(item)
        node.next = self.head # connect next pointer of new node to head
        self.head = node # increment head

    def pop(self):
        if self.head is None:
            print("empty")
            return -1
        val = self.head.val
        temp = self.head
        self.head = self.head.next # head whent backward
        del temp #remove the latest node
        return val
    
    def top(self):
        if self.head is None:
            print("empty")
            return -1
        return self.head.val
    
    def isEmpty(self):
        return self.head is None

class Solution:
    def fun(self, instr, values):
        for i in range(len(instr)):
            if instr[i] == "ArrayStack":
                st = StackUsingLinkedList()
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
instr = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"] 
values =[[], [3], [7], [], [], []]    
sol.fun(instr, values)

# time:- O(1) for all operations (push, pop, top, isEmpty).
# space:- O(n)