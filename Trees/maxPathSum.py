# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi=-99999
    def helper(self, root):
        if root:
            left=self.helper(root.left)
            right=self.helper(root.right)
            max_single = max(max(left, right) + root.val, root.val) 
            max_top = max(max_single, left+right+ root.val)
            self.maxi= max(self.maxi, max_top)
            return max_single
        return 0
            
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.maxi
        