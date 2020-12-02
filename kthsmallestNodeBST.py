# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def count_left(self,left):
        if left:
            count=1
            count+=self.count_left(left.left)
            count+=self.count_left(left.right)
            return count
        else:
            return 0
    def kthsmallest(self, A, B):
        l_depth=self.count_left(A.left)
        if B> l_depth+1:
            return self.kthsmallest(A.right, B-l_depth-1)
        elif B<=l_depth:
            return self.kthsmallest(A.left, B)
        else:
            return A.val