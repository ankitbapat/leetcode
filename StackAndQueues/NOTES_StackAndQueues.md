# Learning
## 1. Implement Stack using Array
#### Code File: ImplementStackUsingArray.py
#### Question:- Implement Stack using Array
#### Input:- instr = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]  ; values = [[], [5], [10], [], [], []]  
#### Output:- [null, null, null, 10, 10, false]  
#### Explanation:-
> constructor:- initialize a list having a fix size, filled with all 0. initialize capacity and index.

> Push:- increment index. assign item to that index of the array. If index is equal to (capacity-1). We could remove size chacek at all to make it simple but it avoid overflow error.

> pop:- return item array at index. reduce index byt 1. if arr.isEmpty() return -1.

> top:- same as pop, but do not reduce index.

> isEmpty:- check if index == -1. 

> Why we do not check len(arr)==0 in isEmpty()? - because the array length is always 1000(capacity) filled with 0's

> Why we have self.capacity? - we maintain self.capacity of the array and do a check in push() if array's self.index reached the self.capacity. If we do not maintain a capacity, it could lead to memory overflow problem as per Low-level design principles!

#### Code:-
    class StackUsingArray:
        def __init__ (self, size=1000):
            self.arr = [0] * size
            self.capacity = size
            self.topIndex = -1

        def push(self, item):
            if self.topIndex >= self.capacity - 1:
                print("stack overflow")
                return
            self.topIndex = self.topIndex + 1
            self.arr[self.topIndex] = item

        def pop(self):
            if self.isEmpty():
                print("stack is empty")
                return -1
            val = self.arr[self.topIndex]
            self.topIndex = self.topIndex - 1
            return val
        
        def top(self):
            if self.isEmpty():
                print("stack is empty")
                return -1
            return self.arr[self.topIndex]
        
        def isEmpty(self):
            return self.topIndex == -1

#### Complexity:-
- time:- O(1) for all operations (push, pop, top, isEmpty).
- space:- O(n)

## 2. Implement Queue using Array
#### Code File: ImplementQueueUsingArray.py
#### Question:- Implement Queue using Array
#### Input:- instr = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"] ; values =[[], [5], [10], [], [], []]   
#### Output:- [null, null, null, 5, 5, false]
#### Explanation:-
> constructor:- initialize a list having a fix size, filled with all 0. initialize capacity and current size. Also 2 indexes (front & back). 

> why did we wrap front and back indexes? - without wrap we would create a "false overflow issue" - e.g. - Capacity is 5. arr size is 5 (filled with all 0's). you Push 5 items (back is 5). you Pop 5 items (front is 5). now push 1 item. back cannot increment beyond the capacity(5). 

> why do we have self.size? - Without it, both an empty queue and a full queue would result in front == back. Since we are wrapping front and back indexes. so we cannot detect isEmpty using front==back logic. So we need self.size to check actual size of queue.

> why front and back indexes? - because we need to push in back and pop from front.

> Push:- assign item to the back index of the arr. instead of linearly incrementing we make a circular queue. so increment(back+1) and do %(mod) with capacity. This is the warpping of back index. Increment current size. if current size == capacity then "queue overflow"

> pop:- return front index element. increment front. wrap it. reduce size. if arr isEmpty, return -1

> peek:- same as pop, but do not reduce front. do not reeuce size

> isEmpty:- check if self.size == 0. 

#### Code:-
    class QueueUsingArray:
        def __init__(self, size=1000):
            self.arr = [0] * size
            self.capacity = size
            self.back = 0
            self.front = 0
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

#### Complexity:-
- time:- O(1) for all operations (push, pop, top, isEmpty) .
- space:- O(n)

## 3. Implement Stack using Queue
#### Code File: ImplementStackUsingQueue.py
#### Question:- Implement Stack using Queue
#### Input:- instr = ["QueueStack", "push", "push", "pop", "top", "isEmpty"] ; values = [[], [4], [8], [], [], []]     
#### Output:-  [null, null, null, 8, 4, false]
#### Explanation:-
> constructor:- initialize a queue(). 

>  push - Take current size of queue. Put item in queue from back. take all items accept the current one from front -> put all of them at the back of the queue. This will make sure that the recent item put into the queue is the first item available at the front of the queue.

> pop - remove the first item of the queue
#### Code:-
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
#### Complexity:-
- time:- O(n) for push and O(1) for all other operations.
- space:- O(n)


## 4. Implement Queue using Stack
#### Code File: ImplementQueueUsingStack.py
#### Question:- Implement Queue using Stack
#### Input:- instr = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]  ; values = [[], [4], [8], [], [], []]     
#### Output:-  [null, null, null, 4, 8, false]
#### Explanation:-
> constructor:- initialize 2 stacks/list. 

>  push - if stack_1 has items - put all of them to stack_2. add item in stack_1. then again put all the items from stack_2 into stack_1. This way first item inserted becomes last one to come out.

> pop - remove the first item from stack_1

> isEmpty - check if stack_1 has items or not.

> In this code always push is O(n). An optimal approach exists where push takes O(1) and pop/peek takes O(n) (however, this O(n) happens rarely)

> In that we push item in stack_1. during pop - we check if stack_2 is empty, then put all items from stack_1 to stack_2. pop from stack_2. 

> why we check if stack_2 is empty - here we balance all the items in both stack_1 and stack_2. if stack_2 is not empty meaning their are elements that needs to be pop() first, than the last element in stack_1. After we pop() all items from stack_2 we start poping items from stack_1. 

> Do the same for peek - instead of pop() return stack_2[-1]

> isEmpty - check if both stack_1 and stack_2 are empty
#### Code:-
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
#### Complexity:-
- time:- O(n) for push and O(1) for all other operations.
- space:- O(n)

## 5. Implement Stack using Linked-List
#### Code File: ImplementStackUsingLinkedList.py
#### Question:- Implement Stack using Single Linked-List
#### Input:- instr = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]  ; values = [[], [3], [7], [], [], []]       
#### Output:-  [null, null, null, 7, 3, false]
#### Explanation:-
> declare a node class

> constructor:- initialize an empty head pointer.  

> push - create new Node(item). assign next pointer of new node to head. move head to new node

> pop - return head.val. before that assign head to temp. move head to head.next. Then del temp. If head==None return -1

> isEmpty - if head==None
#### Code:-
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
#### Complexity:-
- time:- O(1) for all other operations.
- space:- O(n)


## 6. Implement Queue using Linked-List
#### Code File: ImplementQueueUsingLinkedList.py
#### Question:- Implement Queue using Single Linked-List
#### Input:- instr = ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]  ; values = [[], [3], [7], [], [], []]       
#### Output:-  [null, null, null, 3, 3, false]
#### Explanation:-
> declare a node class

> constructor:- initialize an empty start & end pointer & size(for IsEmpty check).  

> push - create a new Node(item). point end.next to new node. move end to new node. If start is None - move both start and end to new node.

> pop - return start.val. before that assign start to temp. move start to start.next. del temp.

> peek - return self.start.val 

> isEmpty - if size==0
#### Code:-
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
#### Complexity:-
- time:- O(1) for all other operations.
- space:- O(n)

## 7. Check if a string has balance parantheses
#### Code File: BalanceParantheses.py
#### Question:- Check if a string has balance parantheses - return True or False
#### Input:- str = “( )[ { } ( ) ]”       
#### Output:-  True
#### Explanation:-
> declare a list/stack. iterate through all the char in the string. put all the open brackets into the stack.

> if we get a close bracket - and if stack is items - pop() if the pop'ed item does not match the open bracket type. return False.

> if we get a close bracket - and if stack is empty - return False

> At the end of the loop, if stack is empty (meaning all the elements matched and the stack is now empty) - return True
#### Code:-
    def fun(self, s):
        st = []
        for i in range(len(s)):            
            if s[i] == "(" or s[i] == "[" or s[i] == "{": st.append(s[i])
            else:
                if st:
                    val = st.pop()
                    if (s[i]==")" and val != "(") or (s[i]=="]" and val != "[") or (s[i]=="}" and val != "{") : return False
                else: return False
        return True if len(st)==0 else False
#### Complexity:-
- time:- O(n)
- space:- O(n)

## 8. Implement Min Stack
#### Code File: MinStack.py
#### Question:- Check if a string has balance parantheses - return True or False
#### Input:- instr = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], items = [ [], [-2], [0], [-3], [ ], [ ], [ ], [ ] ]      
#### Output:-  [null, null, null, null, -3, null, 0, -2]  
#### Explanation:-
> constructer - using 2 stacks. 1 stack to hold all the elemt and another to hold only min elements

> push - add new item to stack. if min_stack has items - put minimum value between (the top item, and the new item). If min_stack is empty - add new item in it.

> pop - pop from both stacks.

> Why this works? - everytime min_stack holds the min_val at the top. if new item is min - we put new item in min_stack. If existing top-elem of min_stack is min - then the same element is pushed again into the stack. maintaining the min_val at the top of the min_stack.

> why we pop from both stacks? - to keep both stacks in sync - if we remove item from original stack, we must remove from min_stack. Because the min_stack always maintain min value till that point. So, to maintain synchronization between the current elements and the minimum value of the stack at that exact moment in time.  

> top - st[-1]. getMin - min_stack[-1].

> this is a brute force. for optimal approach it is a bit complex where min_stack reduced to only 1 variable (see striver code)
#### Code:-
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
#### Complexity:-
- time:- O(1)
- space:- O(n)

# Infix, prefix and postfix- Trick - (Complexity of all the code is O(n) both time and space)
## 9. Infix To Postfix
#### Code File: InfixToPostfix.py
#### Question:- Infix To Postfix
#### Input:-  s =  a + b * (c^d - e) ^ (f + g * h) - i      
#### Output:-  abcd^e-fgh*+^*+i-
#### Explanation:-
> there are pre-defined steps to do this:-

> 1. define the precendance/weight of each operator in a separate func. ^ -> 3, */ -> 2, +- -> 1, rest -> -1

> 2. define a stack and iterate string s

> 3. if operand(a-zA-Z0-9) - push()

> 3. if "(" - push()

> 4. if ")" - keep doing pop() till we get "(". keep adding in res. discard both paranthesis -> ")("

> 5. if operator(+-*/^) -> if stack. and if precedance of stack[-1] is higher or equal s[i] -> keep poping and adding to res. Else push()

> 6. add to res all the rest of the stack elements 
#### Code:-
    def prec(self, c):
        if c == '^':
            return 3
        elif c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1
    def infix_to_postfix(self, s):
        res=""
        st=[]
        for i in range(len(s)):
            if s[i].isalnum(): res = res + s[i]
            elif s[i]=="(":
                st.append(s[i])
            elif s[i]==")":
                while st and st[-1]!="(":
                    res=res+st.pop()
                st.pop() # throw the "("
            else:
                while st and self.prec(s[i]) <= self.prec(st[-1]):
                    res=res+st.pop()
                st.append(s[i])
                    
        while st:
            res = res+st.pop()
        return res

## 10. Infix To Prefix
#### Code File: InfixToPrefix.py
#### Question:- Infix To Prefix
#### Input:-  s =  x + y * z / w + u     
#### Output:-  ++x/*yzwu
#### Explanation:-
> 1. Same as Infix to Postfix, we re-use the code from Infix to Postfix

> 2. first we **reverse** the string. Then we **interchange** open and close bracket. Then we call Infix_To_Postfix. Then we **reverse** again. Then return.

> 3. In Infix To Postfix - there is a slight change instead of (stack[-1] is **higher or equal** s[i]) we do (stack[-1] is **strickly higher** s[i]) - keep poping
#### Code:-
    def prec(self, c):
        if c == '^':
            return 3
        elif c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1
    def infix_to_postfix(self, s):
        res=""
        st=[]
        for i in range(len(s)):
            if s[i].isalnum(): res = res + s[i]
            elif s[i]=="(":
                st.append(s[i])
            elif s[i]==")":
                while st and st[-1]!="(":
                    res=res+st.pop()
                st.pop() # throw the "("
            else:
                while st and self.prec(s[i]) < self.prec(st[-1]):
                    res=res+st.pop()
                st.append(s[i])
                    
        while st:
            res = res+st.pop()
        return res

    def infix_to_prefix(self, infix):
        infix = infix[::-1] # Reverse
        infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')') # Replace '(' with ')' and vice versa
        prefix = self.infix_to_postfix(infix) # Get the postfix of the modified string
        return prefix[::-1]  # Reverse

---

## 11. Postfix To Infix
#### Code File: PostfixToInfix.py
#### Question:- Postfix To Infix
#### Input:-  s =  "ab*cd/+"     
#### Output:-  "(a*b)+(c/d)"
#### Explanation:-
> 1. iterate the string, use stack

> 2. If **operand - push()**

> 3. In **operator** -> **Pop 2** operands -> combine them in **Infix** order -> push()

> 4. return stack[-1]
#### Code:-
    def postfix_to_infix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(f"({a}{i}{b})")
        return st[-1]

## 12. Prefix To Infix
#### Code File: PrefixToInfix.py
#### Question:- Prefix To Infix
#### Input:-  s =  *+ab-cd    
#### Output:-   ((a+b)*(c-d))
#### Explanation:-
> 1. **reverse()** string 

> 2. call Postfix to Infix (slight change - while pushing into stack - push in **Infix** order)
#### Code:-
    def postfix_to_infix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(f"({a}{i}{b})")
        return st[-1]

    def prefix_to_infix(self, s):
        s=s[::-1]
        return self.postfix_to_infix(s)

---

## 13. Postfix to Prefix
#### Code File: PostfixToPrefix.py
#### Question:- Postfix to Prefix
#### Input:-  s = "abc*+d-"    
#### Output:- -+a*bcd
#### Explanation:-
> 1.  iterate the string.

> 2. If **operand - push()**

> 3. In **operator** -> **Pop 2** operands -> combine them in **Prefix** order -> push()

> 4. return stack[-1]
#### Code:-
    def postfix_to_prefix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(i+a+b)
        return st[-1]

## 14. Prefix to Postfix
#### Code File: PrefixToPostfix.py
#### Question:- Prefix to Postfix
#### Input:-  s = "*+ab-cd"    
#### Output:-  ab+cd-*
#### Explanation:-
> 1. **reverse()** string 

> 2. call Postfix to Prefix (slight change - while pushing into stack - push in **Postfix** order)
#### Code:-
    def postfix_to_prefix(self, s):
        st=[]
        for i in s:
            if i.isalnum(): st.append(i)
            else:
                a = st.pop()
                b = st.pop()
                st.append(f"{a+b+i}")
        return st[-1]
    
    def prefix_to_postfix(self, s):
        s=s[::-1]
        return self.postfix_to_prefix(s)


# Monolithic Stack and Queue
## Next Greater Element in an array - 1
#### Code File: NextGreaterElement_1.py
#### Question:- Given an integer array, return the next greater element for every element in the array. The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner. If it doesn't exist, return -1
#### Input:- arr = [1, 3, 2, 4]   
#### Output:- [3, 4, 4, -1]
#### Explanation:-
> 1. we have to find next greater element for each item. Brute force would be to traverse the array twice for each item to get the next greater element

> 2. the intuition is that for every element, we need to know what are the elements towards its righ-hand side. If we know them, then we can find the **next** greater element for that item. 

> 3. We could traverse the array from backwards - so that at each element we would have already traversed all the elements to its right-hand side.

> 4. start from the last item (stack is empty) - the res is -1, coz there is no element to its right. we add that element to the stack (meaning till this point this particular element is the greatest)

> 5. now for other elements, if stack has items and they are less than the current element, then keep poping them till a larger item is found.

> 6. once a larger item is found, add it to res, & also push the current element into stack. 

> 7. If for an element, if no item is found in stack - meaning that there was no larger item found to the right-side of an element. add -1 to res. and push that element into the stack

> 8. the stack always maintains an order - this is monolithic stack (all elements are in one order - decending/ascending). we use this to store the **next** greater element found on the right-hand side for a all the items in the array.
#### Code:-
    def fun_opt(self, arr):
        st=[]
        res=[-1]*len(arr)
        for i in range(len(arr)-1, -1,-1):
            while st and st[-1] <= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(arr[i])
        return res
#### Complexity:-
- time:- O(2n) - outer loop + inner loop (which runs only O(n) times in total for all the elements in the array - for the worst case) 
- space:- O(2n) - res + stack

## Next Greater Element in an array - 2
#### Code File: NextGreaterElement_2.py
#### Question:- same as above - difference is that we use a circular array
#### Input:- arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]   
#### Output:- [10, -1, 6, 6, 2, 6, 7, 7, 9, 9, 10]
#### Explanation:-
> 1. the logic of monotonic stack remains the same but this time it is a circular array . so for all elements we no just have to check till the end of the array but it will go back to index=0 and check for rest of the items in a circular manner - to check for the next greater element.

> 2. for this we double the array - not actually but conceptually . we go from 0 till 2*n-1 in the reverse order same as before

> 3. the current item will be arr[i % n]. but the index will be 2n -1, 2n -2,..1,0 - but the value will be i%n.

> 4. the code is exactly the same, only change is that we add to res, only when (i) is less than (n). 
#### Code:-
    def fun_opt(self, arr):
        st=[]
        n=len(arr)
        res=[-1]*n
        
        for i in range(2*n-1, -1,-1):
            current_element = arr[i % n]
            while st and st[-1] <= current_element:
                st.pop()
            if i < n:
                if st: res[i] = st[-1]
                else: res[i] = -1
            st.append(current_element)  
        return res
#### Complexity:-
- time:- O(4n) - outer loop(2n) + inner loop (which runs only O(2n) times in total for all the elements in the array - for the worst case) 
- space:- O(2n) - res + stack

## Next Smaller Element
#### Code File: NextSmallerElement.py
#### Question:- as the name suggest it is same as next greater element -1 but we have to find smaller instead of greater
#### Input:- arr = [4, 8, 5, 2, 25]
#### Output:- [2, 5, 2, -1, -1]
#### Explanation:-
- this is same as next greater element-1. array is not circular. for last element the res will be -1. Only change is instead of greater we get smaller

- during pop will remove larger elements from array till we find the smaller element - otherwise everything is same! 
#### Code:-
    def fun(self, arr):
        st=[]
        res=[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and st[-1] >= arr[i]:
                st.pop()
            if st:  res[i] = st[-1]
            else: res[i] = -1
            st.append(arr[i])
        return res
#### Complexity:-
- same as next greater element

## Trapping Rainwater
#### Code File: TrappingRainwater.py
#### Question:- Given an array of integers showing elevation of ground. find the water that can be trapped after rain.
#### Input:- height = [0,1,0,2,1,0,1,3,2,1,2,1]
#### Output:- 6
#### Explanation:-
- see striver video for good explanation - the core idea is that for an item the water it can retain after rain will be -> min(leftmax, rightmax) - arr[i] -> meaning, for an item the amount of water is difference between itself and the **minimal** between left-tower(max height item on leftside) and right-tower (max height item on rightside). why min - coz e.g we have 2,0,3 the water at 0 will be 2 not 3. it will overflow if the water at 0 will be 3.  

-  so we do the above for each item and add each item's water retaintion into result. but time complexity will be O(n^2) and space - O(1)

- so we optimize, we create prefix and suffix arrays which indicates what is the left-tower and right-tower at each item. (see video how that prefix and suffix array was derived) - its each basically we just record the max height at each item from lefthand side(iterate array from front) and righthand side(iterate array from back). This way we reduce computation of above formula for each item making time- O(n). but space:- O(n)

- further optimization - where we calculate leftMax and rightMax (prefix and suffix at each item) on the fly. maintaining 2 variables.

- in this approach - we have 2 pointers l and r and we do l++ when arr[l] <= arr[r], else r-- while l<=r (standard iteration of 2 pointers)

- this -  **if arr[l] <= arr[r]** condition:- ensures that there exsist a tower on the right which is either equal to leftMax or greater. so we know that a deep exsists here and the value would be alteast **leftMax-arr[l]** - so we add it to res

- Same in the other case, **else** condition:- which indicates that there exsist a tower on the left which is either equal to rightMax or greater. so we know that a deep exsists here and the value would be alteast **rightMax-arr[r]** - so we add it to res

- we also update leftMax and rightMax on the fly as we iterate through both pointers.
#### Code:-
    def fun(self, arr):
        res=0
        l=0
        r=len(arr)-1
        leftMax=0
        rightMax=0
        while l<=r:
            if arr[l]<=arr[r]:
                if arr[l]>leftMax: leftMax=arr[l]
                else: res=res+leftMax-arr[l]
                l=l+1
            else:
                if arr[r]>rightMax: rightMax=arr[r]
                else: res=res+rightMax-arr[r]
                r=r-1
        return res
#### Complexity:-
- time:- O(n)
- space:- O(1)

## Sum of Subarray Minimums
#### Code File: SumOfSubarrayMinimums.py
#### Question:-  calculate the sum of the minimum value in each (contiguous) subarray of arr
#### Input:- arr = [3, 1, 2, 5]
#### Output:- 18
#### Explanation:-
- So the intuition is that, consider element (3) in the arr [1,4,6,7,3,7,8,1]. the number of subsets it can form in right side is - [3], [3,7], [3,7,8] - for them the smallest number is **3**. for [3,7,8,1] it is 1. 

- similarly for left side, it is - [3], [7,3], [6,7,3], [4,6,7,3], the smallest number is **4**. and for [4,6,7,3,1] it is 1.

- so total number of subsets that we can form for 3 where 3 contributes as min element is **3x4**. So total = 3x4 x 3

- so to get the number of subsets on right and left where that particular element is the smallest - we use the concept of next_smaller_element and previous_smaller_element. 

- we get the difference in the indexes of next_smaller_element and the current number (3) -> those many subsets will be formed, on right-hand-side where that no. (3) is the smallest.

- similarly we do with previous_smaller_element and get no. of subsets of left-hand-side of (3) where 3 is the min element.

- we multiple both sides with the min element (3) to get the contribution of that element (3) towardsthe total.

- we do this with all the elements in the array. and return module of total

- some key points:- while calculating the next_smaller_element -> we consider its indexes and not the actual number (why? coz we need how many subsets can be formed between the given number and the next smallest number). Same for previous_smallest_number.

- also, we do not add -1 if the next_smallest is not found - we add **n**. why? coz - if the next_smallest is not found meaning till the end of the array the current elenment(3) is the smallest. Similary for prevous_smallest we add **-1** indicating no element till the start of the array was smaller than the current element(3)

- also there is an edge case that striver talked in his video. for arr[1, 1]. For this edge case we use **arr[st[-1]] > arr[i]** and not **arr[st[-1]] >= arr[i]** in any one of the definition (next_smaller or previous_smaller)

- With this we can also solve **Sum of Subarray Maximum**
#### Code:-
    def next_smaller_element(self, arr):
        st=[]
        n = len(arr)
        res=[0]*n
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: res[i] = st[-1] 
            else: res[i] = n
            st.append(i)
        return res
    
    def previous_smaller_element(self, arr):
        st=[]
        n = len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st: res[i] = st[-1] 
            else: res[i] = -1
            st.append(i)
        return res
    
    def fun_opt(self, arr):
        nse = self.next_smaller_element(arr)
        pse = self.previous_smaller_element(arr)
        total = 0
        mod = int(1e9 + 7)
        for i in range(len(arr)):
            right = (nse[i] - i)
            left = (i - pse[i])
            val = (left * right * arr[i])
            total = total + val
        return total % mod
#### Complexity:-
- time:- O(2n) + O(2n) + O(n) = O(5n) = O(n) [O(2n) - for each function, O(n) - for main function] 
- space:- O(4n) = O(n) - [2 arrays in 2 funtions, 2 atacks in 2 func]

## Asteroid Collision
#### Code File: AsteroidCollision.py
#### Question:- an array represents an asteroid in a row, determine the state of the asteroids after all collisions. the absolute value represents the size of the asteroid, and the sign represents its direction. All asteroids move at the same speed. When two asteroids meet, the smaller one will explode. If they are the same size, both will explode. Asteroids moving in the same direction will never meet.
#### Input:- asteroids = [10, 5, -3, -8, 7, -6, -7, 12, -15, 20]
#### Output:- [-15, 20]
#### Explanation:-
- In this problem, if we consider (-6) we can see that we check all the previous elements one by one in reverse order(7,-8,-3,5..) - so the datastructure that we can use is LIFO

-  So in this problem we simply use a stack to store all +ve numbers. If we face a -ve then we look into stack and figure out if we want to pop() or push(). the result is in the stack

- Iterate, if +ve push()

- If -ve, then while stack has smaller +ve values -> keep on poping

- If both values are same(absolute value) -> pop() the +ve value in stack

- Else (indicating we have a -ve value with us, and stack has -ve value or stack is empty) -> push() the -ve value in stack
#### Code:-
    def fun(self, asteroids):
        st=[]
        for i in asteroids:
            # push all positive in stack
            if i>0:
                st.append(i)
            # for negatives - do the check with positives in stack
            else:
                while st and st[-1] > 0 and st[-1] < abs(i): # while +ve in stack and value is less -> pop()
                    st.pop()
                if st and st[-1] == abs(i): # if +ve and -ve values are same -> pop() +ves
                    st.pop()
                elif not st or st[-1] < 0: # push() only if - stack is empty, or, already a -ve in stack(same direction)
                    st.append(i)
        return st
#### Complexity:-
- time and space:- O(n) - one loop and one stack

## Sum Of Range Of All Subarray
#### Code File: SumOfRangeOfAllSubarray.py
#### Question:- given an array - we have to find all subarrays and return the sum of all ranges of all the subarrays. the range -> max_value - min_value of the subarray
#### Input:- asteroids = [4, -2, -3, 4, 1]
#### Output:- 59
#### Explanation:-
- This is similar to sum of subarray mins. The intuition is that 

- (sum of all **ranges** of all subarrays) => (sum of **maxs** of all subarrays) - (sum of all **mins** of all subarrays)

-  sum of all **maxs** of all subarrays -> kinda previous problem -> Find all subarray minimums

-  sum of all **mins** of all subarrays -> previous problem -> Find all subarray maximums

#### Code:-
    def nge(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = n
            st.append(i)
        return res
    def pge(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(i)
        return res
    def nse(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = n
            st.append(i)
        return res
    def pse(self, arr):
        st=[]
        n=len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st: res[i] = st[-1]
            else: res[i] = -1
            st.append(i)
        return res
    
    def total_small(self, arr):
        total=0
        nse = self.nse(arr)
        pse = self.pse(arr)
        for i in range(len(arr)):
            left = (i-pse[i]) 
            right = (nse[i]-i)
            val = left * right * arr[i] #no of subsets where i in smaller * arr[i]
            total = total + val
        return total
    def total_large(self, arr):
        total=0
        nge = self.nge(arr)
        pge = self.pge(arr)
        for i in range(len(arr)):
            left = (i-pge[i])
            right = (nge[i]-i) 
            val = left * right * arr[i]  #no of subsets where i in larger * arr[i]
            total = total + val
        return total

    def fun(self, arr):
        return self.total_large(arr) - self.total_small(arr)
        
#### Complexity:-
- time:- O(10n) - double than the previous problem 
- space:- O(8n) - double than the previous problem


## Area of largest rectangle in Histogram
#### Code File: AreaOfLargestRectangleInHistogram.py
#### Question:- Given an array of heights representing the histogram's bar height with width = 1, return the max area formed in the histogram. 
#### Input:- arr = [2,1,5,6,2,3]
#### Output:- 10
#### Explanation:-
- So this uses the same principle of nse and pse.

- For finding the max area that each element covers - we find the next smallest and previous smallest element's indexes. This will get the width of the area.

- width = (left-right-1) and height = arr[i]. So max_area = max(max_area, height*width)
#### Code:-
    def next_smaller_element(self, arr):
        st=[]
        n = len(arr)
        res=[0]*n
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: res[i] = st[-1] 
            else: res[i] = n
            st.append(i)
        return res
    
    def previous_smaller_element(self, arr):
        st=[]
        n = len(arr)
        res=[0]*n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st: res[i] = st[-1] 
            else: res[i] = -1
            st.append(i)
        return res

    def largestRectangleArea(self, arr: List[int]) -> int:
        nse = self.next_smaller_element(arr)
        pse = self.previous_smaller_element(arr)
        max_area = 0
        for i in range(len(arr)):
            right = nse[i]
            left = pse[i]
            area = (right - left - 1) * arr[i]
            max_area = max(max_area, area)
        return max_area
#### Complexity:-
- time:- O(2n) + O(2n) + O(n) = O(5n) = O(n) [O(2n) - for each function, O(n) - for main function] 
- space:- O(4n) = O(n) - [2 arrays in 2 funtions, 2 atacks in 2 func]


## Maximal Rectangle
#### Code File: MaximalRectangle.py
#### Question:- Given a m x n binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area. 
#### Input:- matrix = [["1","0","1","0","0"], ["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"]]
#### Output:- 6
#### Explanation:-
- So this uses the same principle of histogram. We can see that reach row of the matrix represents a histogram.

- Row1 => [1, 0, 1, 0, 0]. Row2 => [2, 0, 2, 1, 1]. Row3 => [3, 1, 3, 2, 2]. Row => [4, 0, 0, 3, 0].

- So what we do is, we iterate throguh each row of a matrix, then each column of that row, 

- we maintain a height array and add 1 to it, if we find matrix[r][c] = 1, or reset it to 0 if we find 0.

- we then pass this height array, for each row, to the **AreaOfLargestRectangleInHistogram** code, to get the max_area of that row.

- we then find max among all of those - then return
#### Code:-
    def fun(self, matrix):
        height=[0]*len(matrix[0])
        final_max_area=0
        for row in matrix:
            for c in range(len(row)):
                if row[c]=="1": height[c] = height[c]+1
                else: height[c] = 0
        
            current_max_area = self.histogram(height)
            final_max_area = max(final_max_area, current_max_area)
        return final_max_area
#### Complexity:-
- time:- time:- O(n x m + n x N) - O(n x m) is O(row x col) -> to iterate through each element in matrix. Also O(N) for histogram max_area finder 
- space:- O(n)


