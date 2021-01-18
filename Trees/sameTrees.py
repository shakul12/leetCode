# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val==q.val:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                    return True
                else:
                    return False
            else:
                return False
        elif (p !=None and q==None) or (q !=None and p==None):
            return False
        return True