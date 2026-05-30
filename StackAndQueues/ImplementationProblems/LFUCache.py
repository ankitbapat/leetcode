class Node:
    def __init__(self, key, val):
        self.next=None
        self.prev=None
        self.key = key
        self.val = val
        self.counter = 1

class List:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def removeNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.size = self.size - 1

    def addNode(self, node):
        temp = self.head.next 
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size = self.size + 1

class LFU:
    def __init__(self, c):
        self.maxSize = c
        self.currSize = 0
        self.leastFreq = 0 # Set least-used frequency
        self.keyNodeDict = {} # hashmap same as LRU
        self.freqListDict = {}  # Hashmap to maintain the lists having different frequencies
    
    def put(self, key, value):
        if self.maxSize == 0:
           return
        
        if key in self.keyNodeDict:
            # self.removeNode(self.dict[key])
            node = self.keyNodeDict[key]
            node.value = value  # Update the value
            self.updateFreqListMap(node)  # Update the frequency
        else:
            if self.currSize == self.maxSize:
                # Remove the least frequently used data-item
               list = self.freqListDict[self.leastFreq]
               del self.keyNodeDict[list.tail.prev.key]
               # Update the frequency map
               self.freqListDict[self.leastFreq].removeNode(list.tail.prev)
               self.currSize -= 1  # Decrement the current size of cache
           
            self.currSize += 1  # Increment the current cache size
            self.leastFreq = 1  
           
            listFreqList = List()
            
            if self.leastFreq in self.freqListDict:
                listFreqList = self.freqListDict[self.leastFreq] # Update the pointer to already present list
           
            node = Node(key, value)
            listFreqList.addNode(node)
            self.keyNodeDict[key] = node
            self.freqListDict[self.leastFreq] = listFreqList
        
    def get(self, key):
        if key in self.keyNodeDict:
            node = self.keyNodeDict[key]
            self.updateFreqListMap(node) # Update the frequency
            # self.removeNode(node)
            # self.addNode(node)
            return node.val
        return -1
    
    def updateFreqListMap(self, node):
       # Remove from Hashmap
       del self.keyNodeDict[node.key]
       
       # Update the frequency list hashmap
       self.freqListDict[node.counter].removeNode(node)
       
       # If node was the last node having its frequency
       if (node.counter == self.leastFreq and self.freqListDict[node.counter].size == 0): 
           self.leastFreq = self.leastFreq + 1
       
       nextHigherFreqList = List()
       
       # If the next higher frequency list already exists
       if node.counter + 1 in self.freqListDict:
           
           # Update pointer to already existing list
           nextHigherFreqList = self.freqListDict[node.counter + 1]
       
       node.counter = node.counter + 1
       
       # Add the node in front of higher frequency list
       nextHigherFreqList.addNode(node)
       
       # Update the frequency list map
       self.freqListDict[node.counter] = nextHigherFreqList
       self.keyNodeDict[node.key] = node

# LFU Cache
cache = LFU(2)

# Queries
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")
cache.put(3, 3)
print(cache.get(2), end=" ")
print(cache.get(3), end=" ")
cache.put(4, 4)
print(cache.get(1), end=" ")
print(cache.get(3), end=" ")
print(cache.get(4), end=" ")


# Time:- get and put both O(1)
# Space:- O(n) - for double LL, and dictionaries