# # Using bit manipulation
# # 000 - 0
# # 001 - 1
# # 010 - 2
# # 011 - 3
# # 100 - 4
# # ...
# # 111 - 7
# class solution:
#     def fun(self, arr):
#         n=len(arr)
#         res=[]
#         for i in range(1<<n):
#             curr=[]
#             for j in range(n):
#                 if (i & 1<<j) != 0:
#                     curr.append(arr[j])
#             res.append(curr)
#         return res

# s=solution()
# arr=[1, 2, 3]
# print(s.fun(arr))

# # time:- (2**n * n) -> outer loop * inner loop
# # space:- O(n)

# Using Recursion - choose/not-choose
# video:- https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6
class solution:
    def fun(self, index, curr, arr, res):
        if index>=len(arr):
            res.append(curr.copy()) #thing to remember
            return
        curr.append(arr[index])
        self.fun(index+1, curr, arr, res)
        curr.pop()
        self.fun(index+1, curr, arr, res)

s=solution()
arr=[3, 1, 2]
res=[]
curr=[]
s.fun(0, curr, arr, res)
print(res)


# Using Recursion - curr will be string
class solution:
    def fun(self, index, curr, arr, res):
        if index>=len(arr):
            res.append(curr)
            return
        # curr.append(arr[index])
        self.fun(index+1, curr + str(arr[index]), arr, res)
        # curr.pop()
        self.fun(index+1, curr, arr, res)

s=solution()
arr=[3, 1, 2]
res=[]
curr=""
s.fun(0, curr, arr, res)
print(res)

# time:- (2**n * n) -> 2**n (2 discussions for each element - choose/not-choose) * time to copy curr into res.
# space:- O(n) -> depth of stack space will be n. If you draw the recursion tree the depth of the tree is n (3,1,2). The tree returns when index==len(arr) and len(arr) = n


