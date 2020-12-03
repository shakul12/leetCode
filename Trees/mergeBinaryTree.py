# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        if A is not None and B is not None:
            A.val= A.val +B.val
            A.left= self.solve(A.left, B.left)
            A.right= self.solve(A.right, B.right)
        elif A is None:
            A=B
        return A