class ListNode:
	def __init__(self,x):
		self.val= x
		self.next= None


class Solution:
	def deleteDuplicates(self, A):
		previous= A
		current= A.next

		while current:
			if previous.val==current.val:
				previous.next=current.next
				current=current.next
			else:
				previous=current
				current=current.next
		return A
