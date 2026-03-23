<------------------------------------------------------PICK / NO-PICK----------------------------------------------------------------------------------->

# 1. Get all Power-Sets/Subsequence
#### Code File: PowerSet.py
#### Input : nums = [1, 2, 3]
#### Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]
#### Explanation:-
> We have to generate all the possible combinations of array [1,2,3]. 
    So we will use recursion and use a decision tree (with a base case) to reach all possible senarios. 
    If the condition matched i.e index == length of curr - then we add it to res.
  
> At each step, we will decide if we want to add an alement or not (PICK/NO-PICK).

> So these are the steps that take place:- 
---
- add the first element in curr. index IS 0. **PICK 1**
- then recursion happens. index BECOMES 1  
- add the second element in curr. index IS 1. **PICK 2** 
- then recursion happens. index BECOMES 2.
- add the third element in curr. index IS 2. **PICK 3**
- then recursion happends. index BECOMES 3 
- base case reached. index IS 3. curr=[1,2,3]. res=[[1,2,3]]. Control returns
---
- control goes back. curr=[1,2,3]. **index BECOMES 2**
- now we do - curr.**pop()**. curr=[1,2]. index IS 2. - This is **BACKTRACKING**
- then recursion happends. **index BECOMES 3**
- base case reached. index IS 3. curr=[1,2]. res=[[1,2,3],[1,2]]. Control returns. We **NOT-PICK 3**.
---
- for loop **ends**. **index WAS 3 BUT NOW BECOMES 2** - We return again.
- now curr=[1,2]. **index AGAIN BECOMES 1**. - *This is how we travel back to the Parent node*
---
- now we do - curr.**pop()**. curr=[1]. **index IS 1** - this is **BACKTRACKING**
- then recursion happends. curr=[1]. **index BECOMES 2**
- now we add third element. curr=[1,3]. **index IS 2**. We **NOT-PICK 2** 
- recursion happens. **index BECOMES 3**
- base case reached. index IS 3. curr=[1,3]. res=[[1,2,3],[1,2],[1,3]]. Control Returns.... 
---
> This continues for the complete decision tree.
#### Code:-
    def fun(self, index, curr, arr, res):
        if index>=len(arr):
            res.append(curr.copy()) #thing to remember
            return
        curr.append(arr[index])
        self.fun(index+1, curr, arr, res)
        curr.pop()
        self.fun(index+1, curr, arr, res)
#### Complexity:-
- Time:- O(2^N) - since we had 2 choices at each step (Pick/No-Pick). Every step == N. so if N is 3 -> 2^3 
- Space:- O(N) - Depth of the recursion tree

<br>

# 2. Generate all Binary Strings
#### Code File: GenerateAllBinaryStrings.py
#### Input:- N=3 
#### Output:- ["000", "001", "010", "011", "100", "101", "110", "111"]
#### Explanation:-
>    We have to generate all the possible binary(0/1) combinations of length N. So we will use recursion and use a decision tree (with a base case) to reach all possible senarios.

>    If the base case is reached we add that array to result.

>    At each step we will decide if we want a 1 or a 0.

>    As curr is a string when we return back we do not need to pop anything, the curr returns to its original state

>    So, we do not need to append() or pop() anything. we can just pass curr+"0" in one call and curr+"1" in another
#### Code:-
    def fun(self, n, curr):
        if len(curr) == n: 
            res.append(curr)
            return

        self.fun(n, curr+"0")
        self.fun(n, curr+"1")
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (1/0). Every step == N. so if N is 3 -> 2^3 
- Space:- O(N) - Depth of the recursion tree

<br>

# 2.a. Generate all Binary Strings Without Consecutive 1s
#### Code File: GenerateAllBinaryStrings.py
#### Input: n = 3
#### Output: ["000", "001", "010", "100", "101"]
#### Explanation:-
>    It is same as the above only with some additional if conditions. If the last element is 1 do not add 1. but add 1 if curr is empty
#### Code:-
    def fun(self, n, curr):
        if len(curr) == n: 
            res.append(curr)
            return

        self.fun(n, curr+"0")
        #1 should be added when curr is empty
        if curr == "":
            self.fun(n, curr+"1")
        #1 should not be added when curr already has elements and last element is 1
        if curr and curr[-1]!="1" : 
            self.fun(n, curr+"1")
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (1/0). Every step == N. so if N is 3 -> 2^3 
- Space:- O(N) - Depth of the recursion tree

<br>

# 3. Get all Power-Sets/Subsequence with SUM=K
#### Code File:- CountAllSubsequencesWithSumK.py 
#### Input:- nums = [4, 9, 2, 5, 1], k = 10
#### Output:- [[4, 5, 1], [9, 1]]
#### Explanation:-
>  Same as the POWER SET only difference is that the base case also keeps track of Sum variable

>  Add element into Sum for Pick and remove from Sum for Not-Pick
#### Code:-
    def fun(self, index, curr, nums, sum, k, res):
        if index==len(nums):
            if sum==k:
                res.append(curr.copy())
            return
        
        curr.append(nums[index])
        sum=sum+nums[index]
        self.fun(index+1, curr, nums, sum, k, res)
        curr.pop()
        sum=sum-nums[index]
        self.fun(index+1, curr, nums, sum, k, res)
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (Pick/No-Pick).
- Space:- O(N) - Depth of the recursion tree

<br>

# 4. Count all Power-Sets/Subsequence with SUM=K (l/r)
#### Code File:- CountAllSubsequencesWithSumK.py
#### Input:- nums = [4, 9, 2, 5, 1], k = 10
#### Output:- 2
#### Explanation:- 
>    Same as Power Set. Difference is when the base condition is satisfied we return 1. Else 0.

>    We add those up when we go back up the tree. 

>    So at the end of the code we return l+r - summing both nodes of a tree and returning the total sum.
#### Code:-
    def fun(self, index, nums, sum, k):
        if index==len(nums):
            if sum==k:
                return 1
            return 0
        
        sum=sum+nums[index]
        l = self.fun(index+1, nums, sum, k)
        sum=sum-nums[index]
        r = self.fun(index+1, nums, sum, k)
        return l+r
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (Pick/No-Pick).
- Space:- O(N) - Depth of the recursion tree

<br>

# 5. Check if there EXISTS a Subsequence with SUM=K (True/False)
#### Code File:- CheckIfThereExistsASubsequenceWithSumK.py
#### Input:- nums = [4, 9, 2, 5, 1], k = 10
#### Output:- True
#### Explanation:- 
>    Same as Power Set. Difference is when the base condition is satisfied we return True. Else False. 

>    And as soon as we hit the base case and find a combo with sum=k. We return True.

>    As soon as we return True - we do not need to traverse rest of the decision tree. 

>    So we keep on returning True back up the tree till we reach root and return True from the root. 

>    So its kinda a break statement - if we found a combo - hit the base case - return true - keep on returning true till the root and break out of the recursion.

>    If the entire decision tree is traversed and we do not hit true - return false at the end of the code. 
#### Code:-
    def fun(self, index, nums, k, sum):
        if index==len(nums):
            if sum==k:
                return True
            return False

        sum=sum+nums[index]
        if self.fun(index+1, nums, k, sum) : return True
        sum=sum-nums[index]
        if self.fun(index+1, nums, k, sum) : return True
        return False
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (Pick/No-Pick).
- Space:- O(N) - Depth of the recursion tree

<br>

# 6. Subset Sum - 1
#### Code File:- SubsetSum-1.py
#### Input: N = 3, arr[] = {5,2,1}
#### Output: 0,1,2,3,5,6,7,8
#### Explanation: 
>   We have to find all the subset’s sum and print them.

>   In this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1] ], so the sums we get will be  0,1,2,3,5,6,7,8.

>   This is much similar to Power set - instead of generating power sets / subsequences. we print the sum of them.

>   We do not maintain and array curr. Instead we can just maintain sum of all. 

>   and we PICK/NO-PICK element to add/not-add into sum.
#### Code:-
    def fun(self, nums, index, sum, res):
        if len(nums)==index:
            res.append(sum)
            return
        self.fun(nums, index+1, sum+nums[index], res)
        self.fun(nums, index+1, sum, res)
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (Pick/No-Pick).
- Space:- O(N) - Depth of the recursion tree

<br>

# 7. CombinationSum - 1
#### Code  File:- CombinationSum-1.py
#### Input: nums = [2,3,6,7], target = 7
#### Output: [[2,2,3],[7]]
#### Explanation:- 
>    We have to return the combination with sum=k but we can choose one element infinite times. the combos should be unique. 

>    So we add item (PICK) only when target>=nums[index]. and we keep PICKing the same element recursively everytime target>=nums[index]==True. 

>    We also reduce target=target-nums[index].

>    If we find that we cannot add the same element again, we choose the next element, target remains as it is, element is not added.

>    we use pop() to backtrack
#### Code:-
    def fun(self, nums, target, index, curr, res):
        if index==len(nums):
            if target==0:
                res.append(curr.copy())
                return
            return

        if target>=nums[index]:
            curr.append(nums[index])
            self.fun(nums, target-nums[index], index, curr, res)
            curr.pop()
        self.fun(nums, target, index+1, curr, res)
#### Complexity:-
    see in the py file

<br>

# 8. GenerateParenthesis
# File:- GenerateParenthesis.py
# Trick
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Explanation:-
    Input is N we have to generate all the possible combinations or valid parenthese. base case is that number of both open and close brackets are equal to n.
    Then add curr to res and return. 
    If number of open brackets is less than n, add "(" to curr and increase the count of open bracket by one. Do a recursion.
    If number of close brackets is less than open, add ")" to curr and increase the count of close bracket by one. Do a recursion.
    We could use array, append "(" / ")" into it and pop it after returning. 
    Or we could just use a string and append "(" / ")" on the recursion call itself. when the call returns we do not need to pop from anything.

Code:-
    def fun(self, n, curr, o, c, res):
        if o==c==n:
            res.append(curr)
            return
        if o<n:
            self.fun(n, curr+"(", o+1,c, res)
        if c<o:
            self.fun(n, curr+")", o,c+1, res)
Complexity:-
    Time:- 2^N - since we had 2 choices at each step (open/close). Every step == N. so if N is 3 -> 2^3 
    Space:- O(N) - Depth of the recursion tree

<----------------------------------------------------------------------------------------------------------------------------------------->



See the SubsequencePatternsTeory.py to learn about some more pattterns:-

Pattern:-
<!-- GenerateAllBinaryStrings - (pick/no-pick)
GenerateAllBinaryStringsWithoutConsecutive 1s - (pick/no-pick)
Print PowerSet / Subsequence - (pick/no-pick)
GetAllSubsequenceWithSumK - (pick/no-pick)
CountAllSubsequenceWithSumK - (pick/no-pick)
CheckIfThereExsistsASubsequenceWithSumK - (pick/no-pick)
CombinationSum-1 (Can take one item infinite time) - pick/no-pick with if condition -->
CombinationSum-2 (Duplicates):- pick using a for loop
CombinationSum-3 (combo of combinationSum 1 and 2)
<!-- SubsetSum-1 (Print sum of subsequences):- pick/no-pick -->
SubsetSum-2 (Duplicates):- combinationSum2
Combinations:- combinationSum2

Trick:-
<!-- GenerateParanthesis: (pick/no-pick) -->
LetterCombinationOfAPhoneNumber:-combinationSum2

countgoodnumber
reverseStack
sortStack

HARD:-
M-coloringProblem:- combinationSum2
PalindromePartitioning:- CombinationSum2
WordBreak:- CombinationSum2
N-Queen:- CombinationSum2

4 directions DFS:-
Word search:- dfs(all 4 directions)
Rate In A Maze:- dfs(all 4 directions)

Sudoku Solver : kinda combinationSum2



# sort on difficulty
# sort on patttern vs tricks
# sort on important problems vs gettingGoodatRecursionProblems
# mark if problem is from 300 list or not
# write logic do not waste time on writing code and complexity, add code blocks/snippest.
# highlight which problems we will have to look because they are very diffcult or use recursion less and other logic more?
# make these notes so they your recursion is done mostly. 
# make it one-stop shop, and, easier, to the point
# make it high level
       