# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root,nodes):
        if root:
            self.inorder(root.left, nodes)
            nodes.append(root)
            self.inorder(root.right, nodes)
        return nodes
    
    def balance(self, nodes, start, end):
        if start>end:
            return None
        mid=(start+end)//2
        node=nodes[mid]
        node.left= self.balance(nodes, start, mid-1)
        node.right= self.balance(nodes, mid+1, end)
        return node
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes=[]
        nodes=self.inorder(root, nodes)
        return self.balance(nodes, 0, len(nodes)-1)
        