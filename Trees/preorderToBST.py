# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preorder):
        #pop element from preorder
        #if no previous then root
        #check if it is smaller that previous
        #true- add to left temp=temp.left
        #false- add to right temp=temp.right
        roots=[]
        root=preorder.pop(0)
        root= TreeNode(val=root)
        temp=root
        #roots.append(root)
        previous=root
        while len(preorder)>0:
            curr=preorder.pop(0)
            curr=TreeNode(val=curr)
            if curr.val<previous.val:
                temp.left=curr
                temp=temp.left
                roots.append(previous)
            else:
                if len(roots)==0:
                    roots.append(previous)
                while len(roots)>0 and curr.val>roots[-1].val:
                    temp=roots.pop()
                temp.right=curr
                temp=temp.right
            previous=curr
        return root
            
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.helper(preorder)
        
                    
            
        