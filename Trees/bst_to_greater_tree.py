# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.base=0
    def helper(self,root):
        if root:
            temp=[]
            while root.right:
                temp.append(root)
                root=root.right
            self.base=root.val+self.base
            root.val=self.base
            if root.left:
                self.helper(root.left)
            while temp:
                node=temp.pop()
                node.val+=self.base
                self.base=node.val
                if node.left:
                    self.helper(node.left)
                    
                
            
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #keep going on right  to find the base
        #keep adding base to root and that becomes new base
        #same process for left tree but with baggage base of root
        self.helper(root)
        return root
        