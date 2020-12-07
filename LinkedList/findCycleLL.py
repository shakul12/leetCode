class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None


class Solution:
	def findCycle(self, A):
		maps= {}
		while A:
			if A in maps:
				return A
			else:
				maps[A]=1
			A=A.next
		return None 