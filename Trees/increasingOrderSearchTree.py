# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if root:
            out=[]
            left=[]
            right=[]
            if root.left:
                left.extend(self.traverse(root.left))
            if root.right:
                right.extend(self.traverse(root.right))
            left.append(root.val)
            return left+right
    def increasingBST(self, root: TreeNode) -> TreeNode:
        out=self.traverse(root)
        new_root= TreeNode(val=out.pop(0))
        temp=new_root
        while len(out)>0:
            temp_node= TreeNode(val=out.pop(0))
            temp.right= temp_node
            temp=temp.right
        return new_root