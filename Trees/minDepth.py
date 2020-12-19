# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def helper(self, root):
        if root:
            if root.left is None and root.right is None:
                return 1
            return min(1+self.helper(root.left),1+self.helper(root.right))
        return 9999999
    def minDepth(self, A):
        return self.helper(A)
            
