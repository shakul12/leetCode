# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        out=[]
        curr=[]
        curr.append(A)
        while len(curr)>0:
            node= curr.pop()
            out.append(node.val)
            if node.right:
                curr.append(node.right)
            if node.left:
                curr.append(node.left)
        return out