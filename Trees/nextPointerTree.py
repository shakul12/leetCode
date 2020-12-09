"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            curr=[]
            curr.append(root)
            next_trav=[]
            while len(curr)>0:
                temp =curr.pop()
                temp_trav=[]
                l= len(curr)
                if l==0:
                    temp.next=None
                else:
                    temp.next= curr[-1]
                if temp.right:
                    temp_trav.append(temp.right)
                if temp.left:
                    temp_trav.append(temp.left)
                next_trav= temp_trav+next_trav
                if len(curr)==0:
                    curr=next_trav
                    next_trav=[]
            return root