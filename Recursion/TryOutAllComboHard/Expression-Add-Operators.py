#see striver solution article
class Solution():    
    def fun(self, start, curr_val, last_operand, expression):

        if start==len(num):
            if curr_val==target:
                res.append(expression)
            return

        for i in range(start, len(num)):
            if i>start and num[i]=="0": return
            curr_num = num[start:i+1] #current number
            curr_num_val = int(num[start:i+1]) #current number value
            if start==0:
                self.fun(i+1, curr_num_val, curr_num_val, curr_num)
            else:
                self.fun(i+1, curr_val + curr_num_val, curr_num_val, expression + "+" + curr_num)
                self.fun(i+1, curr_val - curr_num_val, -curr_num_val, expression + "-" + curr_num)
                self.fun(i+1, curr_val - last_operand + last_operand * curr_num_val, last_operand * curr_num_val, expression + "*" + curr_num)
            

sol=Solution()
target=6
num="123"
operants=['+', '-', '*']
res=[]
sol.fun(0, 0, 0, "")
print(res)