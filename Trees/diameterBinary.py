# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_depth(self,temp, maxi):
        if temp:
            maxi+=1
            maxi= max(self.max_depth(temp.right,maxi), self.max_depth(temp.left,maxi))
            #print(maxi)
        return maxi
    def tree_max(self,root):
        if root:
            return self.max_depth(root.right,0)+ self.max_depth(root.left,0)
        else:
            return 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxi=0
        if root:
            maxi= max(maxi,self.tree_max(root),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return maxi
            
        
        