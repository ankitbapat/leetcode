class Node:
    def __init__(self, key, val):
        self.next=None
        self.prev=None
        self.key = key
        self.val = val

class LRU:
    def __init__(self, c):
        self.capacity = c
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def removeNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def addNode(self, node):
        temp = self.head.next 
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def put(self, key, value):
        if key in self.dict:
            self.removeNode(self.dict[key])

        node = Node(key, value)
        self.dict[key] = node
        self.addNode(node)

        if len(self.dict) > self.capacity:
            n = self.tail.prev
            self.removeNode(n)
            del self.dict[n.key]
        
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
        return -1

class Solution:
    def fun(self, commands, items):
        for i in range(len(commands)):
            if commands[i] == "LRUCache":
                lru=LRU(items[i][0])
                print("null", end=" ")
            elif commands[i] == "put":
                lru.put(items[i][0], items[i][1])
                print("null", end=" ")
            elif commands[i] == "get":
                print(lru.get(items[i][0]), end=" ")

          
sol=Solution()
commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
items = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
sol.fun(commands, items)

# Time:- get and put both O(1)
# Space:- O(n) - for double LL and map