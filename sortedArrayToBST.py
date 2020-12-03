# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if len(A)>=1:
            start= 0
            end= len(A)
            mid=(start+end)//2
            root=TreeNode(A[mid])
            root.left = self.sortedArrayToBST(A[start:mid])
            root.right = self.sortedArrayToBST(A[mid+1:end])
            return root