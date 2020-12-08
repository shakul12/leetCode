class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        nums=[]
        for i in A:
            if i not in '+-/*':
                nums.append(i)
            else:
                exp= '{2}{1}{0}'
                nums.append(int(eval(exp.format(nums.pop(),i,nums.pop()))))
        return nums[0]