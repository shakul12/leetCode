# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,flag):
        if flag:
            if root.right:
                return root.right
            else:
                return None
        else:
            if root.left:
                return root.left
            else:
                return None
    def check(self,left, right):
        while left and right:
            if left.val==right.val:
                return self.check(self.helper(left,False),self.helper(right,True)) and self.check(self.helper(right,False),self.helper(left,True))
            else:
                return False
        if not left and not right:
            return True
    def isSymmetric(self, root: TreeNode) -> bool: 
        if root:
            left= root.left
            right= root.right
            if left and right:
                if self.check(left,right):
                    return True 
            if not left and not right:
                return True
        return False
        