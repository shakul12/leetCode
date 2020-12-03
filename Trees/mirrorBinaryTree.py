class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	def isMirror(self,root1,root2):
		if root1 is None and root2 is None :
			return True
		elif root1 is not None and root2 is not None:
			return ((root1.val==root2.val) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root1.left))
		return False

	def symmetric(self,A):
		return self.isMirror(A,A)
