class Solution():    
    def fun(self, s, curr, ep, last_op, expresion, sum):
        print(expresion)
        if s==len(num):
            if curr==target:
                res.append(expresion)
            return

        for i in range(s, len(num)):
            if i>s and num[i]=="0": return
            n = int(num[s:i+1])
            if s==0:
                self.fun(i+1, curr, n)
            else:
                self.fun(i+1, curr + n, n)
                self.fun(i+1, curr - n, -n)
                self.fun(i+1, curr * n, )
            # if op=='+': sum = sum + int(num[s])
            # if op=='-': sum = sum - int(num[s])
            # if op=="*": sum = sum * int(num[s])
            curr.append(num[s]+op)
            self.fun(s+1, curr, sum)
            curr.pop()
            # if op=="+": sum = sum - int(num[s])
            # if op=="-": sum = sum + int(num[s])
            # if op=="*": sum = sum / int(num[s])


sol=Solution()
target=6
num="123"
operants=['+', '-', '*']
res=[]
sol.fun(0,[],0)
print(res)