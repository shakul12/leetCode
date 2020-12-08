class Solution:
    # @param A : list of integers
    # @return a list of integers

    def prevSmaller(self, A):
        ## stack which has the smallest element in the left
        stack=[]
        out=[]
        
        for i in range(len(A)):
            if len(stack)>0:
                if A[i]>stack[-1]:
                    out.append(stack[-1])
                else:
                    while len(stack)>0 and A[i]<=stack[-1]:
                        stack.pop()
                    if len(stack)==0:
                        out.append(-1)
                    else:
                        out.append(stack[-1])
            else:
                out.append(-1)
            stack.append(A[i])
        return out