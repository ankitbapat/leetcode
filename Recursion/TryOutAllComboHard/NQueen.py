# see the code from Apna college. We have done like them

class Solution():
    def check(self, r,c,n,curr):
            # Note:- here striver says to check lower-left Diagonal, left(backward) & upper-left diagonal. 
            # Apna college solution has checked upper-right diagonal instead.
            
            #Horizontal
            # We would not need horizontal check because we are doing recursion on each row, 
            # and each row is checked from the start weather to keep the queen or not
            
            #Verticle
            for i in range(n):
                if curr[i][c] == "Q": return False
            #Upper-left Diagonal
            i=r
            j=c
            while i>=0 and j>=0:
                if curr[i][j]=="Q": return False
                j=j-1
                i=i-1
            #Upper-right Diagonal
            i=r
            j=c
            while i>=0 and j<n:
                if curr[i][j]=="Q": return False
                i=i-1
                j=j+1

            return True
        
    def fun(self, n, res, curr, r):
        if r==n:
            res.append(["".join(row) for row in curr])
            return
                 
        for c in range(n):
            if self.check(r,c,n,curr): 
                curr[r][c] = "Q"
                self.fun(n, res, curr, r+1)
                curr[r][c]="." 

sol=Solution()
n=4
res = []
curr = [["." for _ in range(n)] for _ in range(n)]
sol.fun(n, res, curr, 0)
print(res)


# Time:- O(N!*N) = 1st queen has N places to fit. second queen has N-1 places to fit. 3rd has N-2 places,..last queen has 1 place to fit
# So the total time complexity is N*(N-1)*(N-2)*...2*1 => N!
# (N!*N) because - the check takes total of O(N) time. So in total:- O(N!*N)

# Space:- O(N*N) + O(N) = result matrix is an array with an array so - N*N. Plus stack space - O(N)


#Optimal Approach - See logic from CodestoryWithMIK for approach 2. He has the same approach as Apna college for approach 1 (recursion on rows for loop on col) 
# In this approach - 
#   We actually use 3 sets to avoid repetative checks we do for each qeen - along the verticle, and 2 diagonals (upper-right & upper-left). 
#   We store the value of column, upper-left and upper-right diagonal as sson as a queen is placed.
#   So for upcomming queens, they will check if there is any other queen on the verticle, and 2 diagonals.
#   We can place the coulmn of a queen in a set easily. But how will we store the upper left and upper right diagonals in the set?
#       -  for the upper-right diagonal - the sum of i+j is same, and, for the upper-left - the difference of i-j is same. 
# The checks from the SETS is done in O(1) time
class Solution(): 

    def fun(self, n, res, curr, r, verticle, upper_right, upper_left):
        if r==n:
            res.append(["".join(row) for row in curr])
            return
                 
        for c in range(n):
            if c not in verticle and (r+c) not in upper_right and (r-c) not in upper_left:
                curr[r][c] = "Q"
                verticle.add(c)
                upper_right.add(r+c)
                upper_left.add(r-c)
                self.fun(n, res, curr, r+1, verticle, upper_right, upper_left)
                curr[r][c]="." 
                verticle.remove(c)
                upper_right.remove(r+c)
                upper_left.remove(r-c)


sol=Solution()
n=1
res = []
curr = [["." for _ in range(n)] for _ in range(n)]
sol.fun(n, res, curr, 0, set(), set(), set())
print(res)

# Time:- O(N!) = 1st queen has N places to fit. second queen has N-1 places to fit. 3rd has N-2 places,..last queen has 1 place to fit
# So the total time complexity is O(N!)

# Space:- O(N*N) + O(N) + O(N) = result matrix is an array with an array so - N*N. Plus stack space - O(N). Plus the 3 sets space
