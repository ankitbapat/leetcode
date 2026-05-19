from collections import deque
class Solution():
    def fun(self, arr, k):
        res = []
        q = deque()
        for i in range(len(arr)):
            # here we check if the front of the queue has index out-of-bound. 
            # so i and previous k elements are in-bound (i-k) -> elements previous to that are out-of-bound
            if q and q[0] <= i-k: 
                q.popleft() # remove from front
            while q and arr[q[-1]] < arr[i]: # keep removing from back - while all elements in queue are smaller
                q.pop()
            q.append(i)
            
            if i>=k-1: # after the first window is passed - start adding the front of the queue in result
                res.append(arr[q[0]])
        return res
sol=Solution()
arr = [4,0,-1,3,5,3,6,8]
k = 3
print(sol.fun(arr, k))

# time:- O(n) - to traval entire array + O(n) - total number of items removed from queue for the entire array traversal
# space:- O(k) - max no. of elements in queue (as we remove the out-of-bound elements)