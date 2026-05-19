class Solution():
    def fun(self, M):
        n=len(M)
        top=0
        bottom=n-1
        while top<bottom:
            if M[top][bottom]==1: top=top+1 #top knows bottom so top cannot be celebrity
            elif M[bottom][top]==1: bottom=bottom-1  #bottom knows top so bottom cannot be celebrity
            else: #  both do not know each other, so both cannot be the celebrity
                top=top+1
                bottom=bottom-1
        if top>bottom: return -1 #bottom crossed top meaning there is no celebrity
        #will use row pointed by top
        for i in range(n):
            if i==top: continue
            # if top knows anyone or anyone does not knows top, return -1. meaning this row is not a celebrity
            if M[top][i]==1 or M[i][top]==0:
                return -1
        return top

sol=Solution()
M = [ 
    [0, 1, 1, 0], 
    [0, 0, 0, 0], 
    [1, 1, 0, 0], 
    [0, 1, 1, 0] 
]
print(sol.fun(M))

# time:-  O(N), since eliminating persons and checking if the last candidate is a celebrity both take O(N) time.
# space:- O(1)