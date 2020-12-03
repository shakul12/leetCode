# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def twoSum(self, nums, target):
        s = set()
     
        for i in range(0, len(nums)):
            temp = target-nums[i]
            if (temp in s):
                return 1
            s.add(nums[i])
        return 0
    
    def get_ele(self,A):
        out=[]
        if A:
            out.extend(self.get_ele(A.left))
            out.append(A.val)
            out.extend(self.get_ele(A.right))
        return out
        
    def t2Sum(self, A, B):
        ele= self.get_ele(A)
        return self.twoSum(ele, B)