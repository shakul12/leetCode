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
    def hasPathSum(self, A, B):
        if A:
            temp= B-A.val
            if A.left==None and A.right==None:
                if temp==0:
                    return 1
                else:
                    return 0
            return self.hasPathSum(A.left,temp) or self.hasPathSum(A.right,temp)
        return 0
