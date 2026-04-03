
# PICK / NO-PICK
- How to think recursively - Whenever the problem is related to picking up elements from an array to form a combination, start thinking about the “pick and non-pick” approach.

## 1. Get all Power-Sets/Subsequence
#### Code File: PowerSet.py
#### Question:- Given a string, find all the possible subsequences of the string.
#### Input : nums = [1, 2, 3]
#### Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]
#### Explanation:-
> We have to generate all the possible combinations of array [1,2,3]. 
    So we will use recursion and use a decision tree (with a base case) to reach all possible senarios. 
    If the condition matched i.e index == length of curr - then we add it to res.
  
> At each step, we will decide if we want to add an alement or not (PICK/NO-PICK).

> So these are the steps that take place:- 
---
> - add the first element in curr. index IS 0. **PICK 1**
> - then recursion happens. index BECOMES 1  
> - add the second element in curr. index IS 1. **PICK 2** 
> - then recursion happens. index BECOMES 2.
> - add the third element in curr. index IS 2. **PICK 3**
> - then recursion happends. index BECOMES 3 
> - base case reached. index IS 3. curr=[1,2,3]. res=[[1,2,3]]. Control returns
> ---
> - control goes back. curr=[1,2,3]. **index BECOMES 2**
> - now we do - curr.**pop()**. curr=[1,2]. index IS 2. - This is **BACKTRACKING**
> - then recursion happends. **index BECOMES 3**
> - base case reached. index IS 3. curr=[1,2]. res=[[1,2,3],[1,2]]. Control returns. We **NOT-PICK 3**.
> ---
> - for loop **ends**. **index WAS 3 BUT NOW BECOMES 2** - We return again.
> - now curr=[1,2]. **index AGAIN BECOMES 1**. - *This is how we travel back to the Parent node*
> ---
> - now we do - curr.**pop()**. curr=[1]. **index IS 1** - this is **BACKTRACKING**
> - then recursion happends. curr=[1]. **index BECOMES 2**
> - now we add third element. curr=[1,3]. **index IS 2**. We **NOT-PICK 2** 
> - recursion happens. **index BECOMES 3**
> - base case reached. index IS 3. curr=[1,3]. res=[[1,2,3],[1,2],[1,3]]. Control Returns.... 
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

## 2. Generate all Binary Strings
#### Code File: GenerateAllBinaryStrings.py
#### Question:- Given an integer n, return all binary strings of length n. Return the result in lexicographically increasing order.
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

## 2.a. Generate all Binary Strings Without Consecutive 1s
#### Code File: GenerateAllBinaryStrings.py
#### Question:- Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the res in lexicographically increasing order.
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

## 3. Get all Power-Sets/Subsequence with SUM=K
#### Code File:- CountAllSubsequencesWithSumK.py
#### Question:- Get all Subsets/subsequences with sum=k 
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

## 4. Count all Power-Sets/Subsequence with SUM=K (l/r)
#### Code File:- CountAllSubsequencesWithSumK.py
#### Question:- count all Subsets/subsequences with sum=k 
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

## 5. Check if there EXISTS a Subsequence with SUM=K (True/False)
#### Code File:- CheckIfThereExistsASubsequenceWithSumK.py
#### Question:- check if there exist a Subsets/subsequences with sum=k 
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

## 6. Subset Sum - 1
#### Code File:- SubsetSum-1.py
#### Question:- return sum of all subsets 
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

## 7. CombinationSum - 1
#### Code File:- CombinationSum-1.py
#### Question:- return the list of all unique combinations where the chosen numbers sum to target. A number can be choosen infinite times
#### Input: nums = [2,3,6,7], target = 7
#### Output: [[2,2,3],[7]]
#### Explanation:- 
>    We have to return the combination with sum=target, we can choose one element infinite times. the combos should be unique. 

>    So we add item (PICK) only when target>=nums[index]. and we keep PICKing the same element recursively everytime target>=nums[index]==True. 

>    We also reduce target=target-nums[index].

>    If we find that we cannot add the same element again, we choose the next element, target remains as it is, element is not added. That is why the next recursion call is outside of the if case. If target is less than num[index], choose the next element

>    we use pop() to backtrack
#### Code:-
    def fun(self, nums, target, index, curr, res):
        if index==len(nums):
            if target==0:
                res.append(curr.copy())
            return

        if target>=nums[index]:
            curr.append(nums[index])
            self.fun(nums, target-nums[index], index, curr, res)
            curr.pop()
        self.fun(nums, target, index+1, curr, res)
#### Complexity:-
- time:- O(2^T) * K -> 2^T meaning - 2 to the power target(T). Why coz you keep on picking and non-picking till the target reduces to 0.
Assume your nums=[1] and Target is 10. The complexity of pick/not-pick will be 2^T. We can pick/not-pick T times. K length of curr to copy

- space:- O(k * X) -> the space complexity is variable and dependents on number of combinations generated (X). k-> size of curr. 
k (size of curr) * X (number of curr)

## 8. GenerateParenthesis (Trick)
#### Code File:- GenerateParenthesis.py
#### Question:- Given n pairs of parentheses, generate all combinations of well-formed parentheses.
#### Input: n = 3
#### Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#### Explanation:-
>    Input is N we have to generate all the possible combinations or valid parenthese. base case is that number of both open and close brackets are equal to n.

>    Then add curr to res and return. 

>    If number of open brackets is less than n, add "(" to curr and increase the count of open bracket by one. Do a recursion.

>    If number of close brackets is less than open, add ")" to curr and increase the count of close bracket by one. Do a recursion.

>    We could use array, append "(" / ")" into it and pop it after returning. 

>    Or we could just use a string and append "(" / ")" on the recursion call itself. when the call returns we do not need to pop from anything.
#### Code:-
    def fun(self, n, curr, o, c, res):
        if o==c==n:
            res.append(curr)
            return
        if o<n:
            self.fun(n, curr+"(", o+1,c, res)
        if c<o:
            self.fun(n, curr+")", o,c+1, res)
#### Complexity:-
- Time:- 2^N - since we had 2 choices at each step (open/close). Every step == N. so if N is 3 -> 2^3 
- Space:- O(N) - Depth of the recursion tree

<br>

# PICK or NOT using For-loop
- In this the decision tree has N choises at each level. In the PICK/NO-PICK category the tree has 2 choices at each level (PICK the element or Not-PICK the element). 
- Here, we have N choices at each level - meaning - at each level of the decision tree we go over N elements and decide if we Pick one element or move to the next element. If we PICK ( lets say the 1st element ) we then go further down (one more level) the decision tree, and, decide weather to choose the next elements or not (given that we already choose the 1st element). At this level we loop from 2nd element till last and decide to Pick the elements or not. If yes, then we picked 1st & 2nd elements, not we go further down and check if we could pick from 3rd elem till last... and so on! 

## 9. CombinationSum - 2 
#### Code File:- CombinationSum-2.py
#### Question:- return the list of all unique combinations where the chosen numbers sum to target. A number can be choosen once in the combo
#### Input: nums = [10,1,2,7,6,1,5], target = 8
#### Output: [[1,1,6], [1,2,5], [1,7],  [2,6]]
#### Explanation:-
> We have to return the combination where sum=target. the combos should be unique. input contains duplicates. we choose only one element at a time(unlike combinationSum 1).

> We sort the array to ensure combinations are in sorted order and to avoid duplicates.

>  So here in our decision tree, we pick 1st element and one step down the tree we pick all the remaining elements starting from the 2nd element till end. Once we pick 2nd element, we go one step further down and pick from 3rd element till last, and so on... 

> So we use a for-loop and call recursion inside it, passing (i+1) as index and reducing target as target-nums[index].

> Inside the for-loop we decide if the element is not duplicate(i != i-1) and it is smaller than target. If nums[index] > target, we break out of the loop. 

> We do the break thing, because if the current elem is larger than target, we need not check its next elements as they all will be larger than target. This happens because nums is sorted.

> We do add the element to curr and pop it back while returning for Backtraking. If target=0, add curr to res. 
#### Code:-
    def fun(self, nums, target, index, curr, res):
        if target==0:
            res.append(curr.copy())
            return
        for i in range(index,len(nums)):
            if target<nums[i]:
                break;
            if i > index and nums[i]==nums[i-1]: 
                continue;
            curr.append(nums[i])
            self.fun(nums, target-nums[i], i+1, curr, res)
            curr.pop()

    nums=sorted(nums)
#### Complexity:-
- Time:- 2^n * K - 2^n subsequences, storing takes O(k) time where k is the average length of each combination.
- Space:- O(k * X) -> number of combinations generated (X) * k-> size of curr. 

## 10. CombinationSum - 3 
#### Code File:- CombinationSum-3.py
#### Question:- get all possible set of k numbers that can be added together to equal n.  k = 1-9. only one number can be choosen from 1-9
#### Input:  k = 3, n = 7
#### Output: [[1, 2, 4]]
#### Explanation:-
> It is a combo of combination sum 1 and 2. Give all possible set of k numbers that can be added together to equal n. k is 1 to 9. each number can be choosen once 

> we use the same logic as combinationSum-2. We pick the first elem (1), do a recursion, one step down the decision tree, we try all elements from 2 till 9. then we pick 2, we go down the tree and try for all elements from 3 till 9. and so on...

> we check if the sum==target and len(curr)==k - we add curr to res

> inside the forloop if sum+nums[i]>target - we break. no need to check for further elements because they are anyways all greater
#### Code:-
    def fun(self, nums, target, k, curr, sum, index, res):
        if sum==target and len(curr)==k:
            res.append(curr.copy())
            return
        
        for i in range(index, 10):
            if sum+nums[i]>target: break
            curr.append(nums[i])
            self.fun(nums, target, k, curr, sum+nums[i], i+1, res)
            curr.pop()
    
    nums = [1,2,3,4,5,6,7,8,9]
#### Complexity:-
- Time:- O(2^9 * k):- 2^9 comniations at each step. Plus k to copy the curr of length k into result
- Space:-  O(k) - The maximum depth of the recursion tree is k, as we are only looking for a combination of k numbers. 

## 11. SubsetSum - 2 
#### Code File:- SubsetSum-2.py
#### Question:- Given nums, it can have duplicate, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any order.
#### Input:  nums=[1,2,2]
#### Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
#### Explanation:-
> Given an integer array nums, which can have duplicate entries, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.

> Same as combination sum 2

> Instead of generating all subsets and then removing duplicates, we can avoid creating duplicates in the first place. This is done by sorting the input array first so that all duplicate numbers are adjacent. if nums[i]==nums[i-1]: continue

> we choose 1st then down the tree we choose 2 till last. then down the tree we choose 3 till last, and so on..

> no base case needed as we need all the posssible subsets
#### Code:-
    def fun(self, nums, index, curr, res):
        res.append(curr.copy())

        for i in range(index, len(nums)):
            if i>index and nums[i]==nums[i-1]: continue
            curr.append(nums[i])
            self.fun(nums, i+1, curr, res)
            curr.pop()
    
    nums.sort()
#### Complexity:-
- Time:- O(2^n) - for no. of combinations
- Space:-  O(2^n) - for no. of combinatinations to be stored + O(n) stack space 

## 12. Combinations
#### Code File:- Combinations.py
#### Question:- Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#### Input:  n = 4, k = 2
#### Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#### Explanation:-
> Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

> Same as combination sum 2

> we choose 1st then down the tree we choose 2 till last. then down the tree we choose 3 till last, and so on..

> if len(curr)==k we hit the base case. add curr to res
#### Code:-
    def fun(self, curr, start):
        if len(curr)==k:
            res.append(curr.copy())
            return
        for i in range(start,n+1):
            curr.append(i)
            self.fun(curr, i+1)
            curr.pop()
#### Complexity:-
- Time:- O(2**n) * O(k) - same as combination sum 2
- Space:-  O(k * x) - same as combination sum 2 

## 13. LetterCombinationOfAPhoneNumber (Trick)
#### Code File:- LetterCombinationOfAPhoneNumber.py
#### Question:- Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.
#### Input: digits = "23"
#### Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#### Explanation:-
> we have to return all the combinations of strings that is associated with a digit on a telephone-pad. input will be the digits.

> similar to combination sum 2. We build a map first to have all the digits and there corresponding strings.

> we iterate through each char of 1st digit in the for-loop. So we pick 1st char of 1st digit. then do recursion on 1st char of 2nd digit. base case add - 1st char of 1st digit and 1st char of 2nd digit. Now return - pop the 1st char of 2nd digit - add 2nd char of 2nd digit - recursion - base case - return - pop 2nd char of 2nd digit - add 3rd char of 2nd digit ... base case - loop end - now try 2nd char of 1st digit and then in for-loop try all chars one-by-one of 2nd digit. now the same with 3rd char of 1st digit..finally we get all the combos.
#### Code:-
    def fun(self, d_index, curr, res, digits, map_digits):
        if d_index==len(digits):
            res.append(curr)
            return
        
        st = map_digits[digits[d_index]]
        for i in range(len(st)):
            # curr.append(st[i])
            self.fun(d_index+1, curr+st[i], res, digits, map_digits)
            # curr.pop()

    digits = "23"
    map_digits = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
#### Complexity:-
- Time:- O(N^D) * N - number of digits (D). length of string(abc,def,etc..) (N). multiplied by N coz concatenating each string takes N time. For example:- 3 places 2 choises to make at each place. complexity is "2^3". total 8 choices
- Space:-  O(D) - stack space depth (number of digits (D)). Space complexity could also be O(N^D)*O(N) because N^D * N are the total combinations that gets generated. But we take stack-space into consideration instead of space required to store the result

## 14. M-coloringProblem (Hard Problem)
#### Code File:- M-ColoringProblem.py
#### Question:- Given an undirected graph and a number m, check if the graph can be colored with at most m colors such that no two adjacent vertices are of same color.
#### Input: Edges[] = {  (0, 1),  (1, 2),  (2, 3),  (3, 0),  (0, 2)  } M = 3 
#### Output: 1. - It is possible to color the given graph using 3 colors, so the answer is 1 (possible).
#### Explanation:-
> Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with the same color.

> Simliar to combinationSum-2. We try every color at each node. so a for-loop for every color. We check if we can apply 1st color or 2nd or 3rd..so on.

> we write a separate func to check if a color can be applied or not. constriants - no two adjacent nodes can have the same color.

> if yes then, do recursion and check for the next node and so on...  Base case if index==N (total number of nodes)

> Return true at base case and return at the recursion call itself - since we just have to check if A solution exists or not (similar logic as question 5)

> TO check if we can apply a colo to the node ot not - we maintain a map = {node:edges}. Using this map we check if the same color does not exists in the adjacent node.
#### Code:-
    def canApplyColorToNode(self, c, n, node_to_color):
        for e in edges[n]:
            # Check if adjacent node has the same color
            if e in node_to_color and node_to_color[e]==c: return False
        return True 
    
    def fun(self, node, node_to_color):
        if node==N: return True
        for c in range(M):
            if self.canApplyColorToNode(c, node, node_to_color):
                node_to_color[node]=c
                if self.fun(node+1, node_to_color): 
                    return True
        return False
    
    edges = {i:[] for i in range(N)}
    for u, v in edges_set:
        edges[u].append(v)
        edges[v].append(u)

    fun(0,{},)
#### Complexity:-
- Time:- O(C^N) - C number of colors. N number of nodes
- Space:- O(N) - depth of rec stack -> length of nodes

## 15. PalindromePartitioning (Hard Problem)
#### Code File:- PalindromePartitioning.py
#### Question:- Given a string s partition it such that every substring of partition is palindrome. Return all possible palindrome partition of string s.
#### Input: s = "aabaa"
#### Output: [ [ "a", "a", "b", "a", "a"] , [ "a", "a", "b", "aa"] , [ "a", "aba", "a"] , [ "aa", "b", "a", "a"] , [ "aa", "b", "aa" ] , [ "aabaa" ] ]
#### Explanation:-
> Given a string, partition it such that every substring of the partition is palindrome. Return all possible palindrome partition of the string.

> similar to combinationSum-2 we try out all the substrings. So will choose 1st char and check for any of the substrings from 1st char till last is a plaindrome - if yes then - do recursion - and check if any of the substrings from 2nd char till last is palindrome. here we go one-step down the decision tree. If yes, then - do recurion again - and check if any substring from 3rd char till last is a substrings - here we go further down. then we check from 4th till last and so on.. 

> base case - by going down the recursion tree level-by-level, we reach a base case were the element reaches the end of the string so index==len(s). at this stage we add curr to res.

> we do pop to backtrack
#### Code:-
    def isPalindrome(self, s):
        return s==s[::-1]
    
    def fun(self, s, index, curr, res):
        if index==len(s):
            res.append(curr.copy())
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s[index:i+1]):
                curr.append(s[index:i+1])
                self.fun(s, i+1, curr, res)
                curr.pop()
#### Complexity:-
- Time:- O(2^len(s) * s) -> 2^len(s) at each step we decide weather to pick or not pick a character. Also for calculating palindrome we need O(len(s))
- Space:- O(len(s)) -> stack depth

## 16. WordBreak (Hard Problem)
#### Code File:- WordBreak.py
#### Question:- Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#### Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] OR s = "aaaaaaa", wordDict = ["aaa", "aaaa"]
#### Output: True
#### Explanation:-
>  this is similar to combination sum 2 logic. for every char of string we try out all the words from the wordDict. So here we use each word in the dictionary in the for-loop

> so we take 1st element in the string and check if substring from 1st element till len(word) == any word. if yes, then do recursion - one level down the tree - check for 2nd element in the string, if the substring from 2nd element till len(word) == any word . if yes then go down check substring 3rd till len(word) == any word. ..so on. 

> base case when we reach len(s) we found that all elements from string(s) can be build using all the words from dict. return True

> return True in recursion call - break if base case s reached - else if base case is not reached at the end of the function return False.
#### Code:-
    def fun(self,i):
        if i==len(s): return True
        for w in wordDict:
            if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                if self.fun(i+len(w)): 
                    return True
        return False
#### Complexity:-
- Time:- O(L x W^S) -> W are the words and S is the length of string. At each character we can make W choices. so O(W^S). Now length of longest word in dict is L. So to check a word of length L at each step (position),
- Space:- O(S) -> stack depth

## 17. N-Queen (Hard Problem)
#### Code File:- NQueen.py
#### Question:- placing n queens on n × n chessboard such that no two queens can attack each other.
#### Input: N = 4
#### Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#### Explanation:-
> NOTE:- This is a brute force. See the codefile for optimal approach

>  Similar to combinationSum2. In this problem check for each row can we place queen for any of its column. So a for loop on column and if yes, then do recursion on next row. kep doing this till base case - row==N. meaning our row count reached N, so we not add curr to res. use pop for backtracking

> we check if we can place the queen in verticle and horizontal direction easily (we avoid horizontal coz it is redundant check)

> to check for diagonals we check for upper-left and upper-right diagonals

> A more optimized approach is shown in the code file which uses less time. So code file for it
#### Code:-
    def check(self, r,c,n,curr):
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

    curr = [["." for _ in range(n)] for _ in range(n)]
    sol.fun(n, res, curr, 0)
#### Complexity:-
- Time:- O(N! x N) = 1st queen has N places to fit. second queen has N-1 places to fit. 3rd has N-2 places,..last queen has 1 place to fit. So the total time complexity is N x (N-1) x (N-2) x ...2 x 1 => N!. Now, each check takes total of O(N) time. So in total:- O(N! x N)
- Space:- O(N x N) + O(N) = result matrix is an array with an array so - N x N. Plus stack space - O(N)


## 18. SudokuSolver (Hard Problem) (Trick)
#### Code File:- SudokuSolver.py
#### Question:- create a program to solve sudoku - For every row, column and 3*3 grid - the no. from 1-9 should appear only once. empty cell is "."
#### Input:- board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#### Output:- [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]] 
#### Explanation:-
>  This is a hard problem and we iterate through each "." element and check if we could add any number from 1-9 at that place. We check by row and col and by 3*3 grid.

> if we could then we add that number at that position - then we do recursion - in the recurion we do not pass anything. the for loops we check if the current element is "." only then check if we can put any number(1-9). if not "." then the loop increments and we try next element.

> this is how we check each and every element in the matrix. If we try each number from 1-9 and we cannot fit any number we return false. 

> at the end of all the loops we return true - this is the base case. were we say that all elements are done and we tried all numbers 1-9 at each step - now return True. We return True if the recurion call itself returns true.

> to check into grid - 3*3 we divide the row and col by 3 and multiple by 3 to get new_row and new_col. we then iterate for each element in the grid starting from new_row and new_col till new_row+3 and new_col+3.
#### Code:-
    def check(self, r,c,v):
        # for this check see the solution from apna college
        for j in range(9):
            if board[r][j] == v:
                return False #check next number in values, and also skip row and small-matrix check
        for i in range(9):
            if board[i][c] == v:
                return False #check next number in values, and also skip row and small-matrix check
        sr=3*int(r/3)
        sc=3*int(c/3)
        for i in range(sr, sr+3):
            for j in range(sc, sc+3):
                if board[i][j] == v:
                    return False #check next number in values, and also skip row and small-matrix check
        return True


    def fun(self, board): 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    for v in values:
                        if self.check(r,c,v):
                            board[r][c]=v
                            if self.fun(board): return True
                            board[r][c]="."
                    return False
        return True #base case

    board = [
        [5,3,".", ".",7,".", ".", ".", "."],
        [6,".",".", 1,9,5, ".", ".", "."],
        [".",9,8, ".", ".", ".", ".",6,"."],
        [8,".",".", ".",6,".", ".", ".",3],
        [4,".",".", 8,".",3, ".", ".",1],
        [7,".",".", ".",2,".", ".", ".",6],
        [".",6,".", ".", ".", ".", 2,8,"."],
        [".",".",".", 4,1,9, ".", ".",5],
        [".",".",".", ".",8,".", ".",7,9]
    ]
    values = [1,2,3,4,5,6,7,8,9]
    COLS=len(board[0])
    ROWS=len(board)
    sol.fun(board)
    print(board)
#### Complexity:-
- Time:- O(9^n^2) + O(n^2). 9 digits to choose. 9 branches of a decision tree. for every element in a matrix -> n^2. O(n^2) for checking function.
- Space:- the recurion depth is :-
    - Recursion depth - O(81) - O(1) - since there are total 81 cells
    - Board Storage - O(1) - in-place board modification

<br>

# 4 Direction DFS

## 19. Word Search (Hard Problem)
#### Code File:- WordSearch.py
#### Question:- Given an m x n grid, return true if the word exists in the grid. You can search horizontal and verticle
#### Input:- word = "ABCCED", matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
#### Output:- True 
#### Explanation:-
>  Note there is a optimal approach available which do not use set. It stores the matrix element in temp, and marks it with a char('#'). While returning(backtracking), the temp is then written back on that matrix element. this avoids the use of set (to keep track of visited elements). Look at the codeFile for the solution

> In this code, we traverse through each element of the matrix, and do DFS in 4 directions for each cell.

> as we call DFS for that element, we add that element in set, and do dfs on 4 different directions -> UP,DOWN,RIGHT,LEFT for the next element in word(index+1). We remove from the set when we do backtracking. This is the same pattern that we follow in subsets/combinationSum-2 -> curr.add(), recursion, curr.pop() -> basically this is how we do recursion in almost all problems

> base case if if the index==len(word - basically we reach the last element) -> return True

>we also check if r and c are within bounds and the element is not already visited and the element matches the element in the matrix. If not then return False

> A logical OR of DFS for all 4 directions - gives us res - which we return at the end of recursion
#### Code:-
    def fun(self, matrix, word):

        def dfs(r ,c, index):
            if index==len(word): return True
            
            if r not in range(0,ROWS) or c not in range(0,COLS) or ((r,c) in st) or matrix[r][c]!=word[index]: 
                return False
            
            st.add((r,c))
            res = dfs(r,c+1,index+1) or dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c-1,index+1)
            st.remove((r, c))

            return res
        
        ROWS=len(matrix)
        COLS=len(matrix[0])
        st=set()
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False
#### Complexity:-
- Time:- O(n^2)*O(4^len(word)) - using 2 for loops + 4 choises at each element during recursion.
- Space:- O(len(word)) + O(set) - recurion depth + used space for SET

## 20. Rate In A Maze (Hard Problem)
#### Code File:- RateInAMaze.py
#### Question:- A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1). Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).
#### Input:- n = 4 , grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
#### Output:- ["DDRDRR" , "DRDDRR"] 
#### Explanation:-
>  Note there is a optimal approach available which do not use set. It stores the matrix element in temp, and marks it with a char('#'). While returning(backtracking), the temp is then written back on that matrix element. this avoids the use of set (to keep track of visited elements). Same as the previoius question

> This is similar to the word search - where, we traverse through each element of the matrix, and do DFS in 4 directions for each cell.

> as we call DFS on that grid element, we add that element in set, and do dfs on 4 different directions -> UP,DOWN,RIGHT,LEFT and update/increment the row or column by 1. We remove from the set when we do backtracking. This is the same pattern that we follow in subsets/combinationSum-2 -> curr.add(), recursion, curr.pop() -> basically this is how we do recursion in almost all problems

> base case if the we reach the end of the grid (r==c==n-1) -> add curr to res and return

> we also check if row and column are within bounds and the element is not already visited and the the grid element is not 0. If not then return

> A logical OR of DFS for all 4 directions - gives us res - which we return at the end of recursion
#### Code:-
    def fun(self,r,c,curr):
        if r==n-1 and c==n-1:
            res.append(curr)
            return
        
        if r<0 or c<0 or r>=n or c>=n or ((r,c) in st) or grid[r][c] == 0: return

        st.add((r,c))
        self.fun(r,c+1, curr+"R") or self.fun(r,c-1, curr+"L") or self.fun(r+1,c, curr+"D") or self.fun(r-1,c, curr+"U")
        st.remove((r,c))
    
    if grid[0][0] == 1: 
        sol.fun(0,0,"")
#### Complexity:-
- Time:- O(4^N x M) - N x M are the positions. At reach position the mouse takes 4 directions. 4^N*M
- Space:- O(N*M) - stack space

<br>

# Getting Strong in recursion

## 21. Count Good Numbers (Trick)
#### Code File:- CountGoodNumbers.py
#### Question:- A digit string is considered good if the digits at even indices are even digits (0, 2, 4, 6, 8) and the digits at odd indices are prime digits (2, 3, 5, 7). return the total number of good digit strings of length n. As the result may be large, return it modulo 109 + 7.
#### Input: n=2
#### Output: 20
#### Explanation:-
>  see the explanation from link - https://algo.monster/liteproblems/1922

> since the length is given as input - as n. (n+1)//2 becomes all even positions and n//2 becomes all odd positions. 

> we then return pow of 5 at even places and 4 at odd places. we use MOD for each even and odd place - return multiplication of both. Finally, the res is MOD again.

#### Code:-
    def fun(self,n):
        MOD = 10**9+7
        even_places = (n+1)//2          # Ceiling of n/2
        odd_places = n//2               # Floor of n/2
        return ( pow(5, even_places, MOD) * pow(4, odd_places, MOD) ) % MOD
#### Complexity:-
- Time:- log(n) -  This is because the built-in pow function with three arguments uses fast exponentiation
- Space:- O(1)

## 22. Reverse A Stack (Trick)
#### Code File:- ReverseAStack.py
#### Question:- reverse a stack
#### Input: [4, 1, 3, 2]
#### Output: [2, 3, 1, 4]
#### Explanation:-
> If stack is present - pop - call recursion. So using this we first pop all the lements from the stack. 

> then stack is empty - so backtrack - we now insert each item one by one in revere order. here at the backtrack step the last element in the stack is the one that we have with us.

> in the insert funtion - if stack is empty add the value - so the first value (which is technically the last value) gets added

> we then return - now the control goes to main func - backtrack - we now have the second last element with us. we call insert func with the 2nd-last element.

> inside the insert function - the element which is already present in the stack is removed (this is the element which we inserted before "the last-element")

> we then recurse to see if the stack is empty - yes then we append 2nd last element in stack - backtrack and append last element on top again

> So using the recurion - we first pop all items - call insert for each of them - an insert them in reverse order using another recursion loop
#### Code:-
    def insert_at_last(self, stack, temp):
        if not stack:
            stack.append(temp)
            return
        
        val = stack.pop()
        self.insert_at_last(stack, temp)
        stack.append(val)

    def reverseStack(self, stack):
        if stack:
            temp = stack.pop()
            self.reverseStack(stack)
            self.insert_at_last(stack, temp)
#### Complexity:-
- Time:- O(n^2)
- Space:- O(n)

## 23. Sort A Stack (Trick)
#### Code File:- SortStackWithRecursion.py
#### Question:- sort the stack
#### Input: [4, 1, 3, 2]
#### Output: [1, 2, 3, 4]
#### Explanation:-
>  This isa same as before only diff is that - inside the insert function - we check if the items already in the stack are smaller than the one we have with us. and stack is not empty. only then we append the element (this way we ensure the sorting)
#### Code:-
    def insert(self, stack, temp):
        if not stack or stack[-1] <= temp:
            stack.append(temp)
            return
        
        val = stack.pop()
        self.insert(stack, temp)
        stack.append(val)

    def sortStack(self, stack):
        if stack:
            temp = stack.pop()
            self.sortStack(stack)
            self.insert(stack, temp)
#### Complexity:-
- Time:- O(n^2)
- Space:- O(n)

<br>

# Summary
### Pick/no-pick
- GenerateAllBinaryStrings
- GenerateAllBinaryStringsWithoutConsecutive 1s
- Print PowerSet / Subsequence / Subsets-1
- GetAllSubsequenceWithSumK - (return 1/0)
- CountAllSubsequenceWithSumK - (return T/F)
- CheckIfThereExsistsASubsequenceWithSumK
- CombinationSum-1 - (Can take one item infinite time - pick/no-pick with if condition)
---
### Pick using For-loop
- CombinationSum-2 - (Duplicates)
- CombinationSum-3 - (Combo of combinationSum 1 and 2)
- SubsetSum-1 - (print sum of all subsets)
- SubsetSum-2 - (print sum of all subsets with Duplicates)
- Combinations
- M-coloringProblem (HARD)
- PalindromePartitioning (HARD)
- WordBreak (HARD)
- N-Queen (HARD)
- SudokuSolver (HARD)
---
### 4 Directions DFS
- WordSearch (HARD)
- Rate In A Maze (HARD)
---
### Trick
- GenerateParanthesis - (pick/no-pick)
- LetterCombinationOfAPhoneNumber - (Pick using For-loop)
- countgoodnumber - (recursion)
- reverseStack - (recursion)
- sortStack - (recursion)
---
### Extreme HARD
- Expression-Add-Operator (VERY HARD)
---
---
### DSA Sheet Questions included
- LetterCombinationOfAPhoneNumber
- Combinations
- CombinationSum-1
- GenerateParanthesis
- WordSearch
- Subsets-1
- PalindromePartitioning
- CombinationSum-2
- Subsets-2
- N-Queen
### DSA Sheet Questions NOT included
- Permutations
- N-Queen-2 (HARD)
- Remove Invalid Parentheses (HARD)
- Wildcard Matching (HARD)
- Regular Expression Matching (HARD)


<!-- # sort on difficulty
# sort on patttern vs tricks
# sort on important problems vs gettingGoodatRecursionProblems
# mark if problem is from 300 list or not
# write logic do not waste time on writing code and complexity, add code blocks/snippest.
# highlight which problems we will have to look because they are very diffcult or use recursion less and other logic more?
# make these notes so they your recursion is done mostly. 
# make it one-stop shop, and, easier, to the point
# make it high level -->
       