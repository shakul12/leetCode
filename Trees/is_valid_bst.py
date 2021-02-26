class Solution:
	def helper(self,root,mini,maxi):
		if root:
			if root.val<mini or root.val>maxi:
				return False
			return self.helper(root.left, mini, root.val-1) and self.helper(root.right, root.val+1,maxi)
		return True
	def is_valid_bst(self,root):
		return self.helper(root, -4294967296, 4294967296)
