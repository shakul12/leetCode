class Solution:
	def slidingWindow(self, A, B):
		out=[]
		queue=[]
		for i in range(B):
			while queue and A[i]>=A[queue[-1]]:
				queue.pop()
			queue.append(i)
		for i in range(k,len(A)):
			out.append(A[queue[0]])
			while queue and queue[0]<i-B:
				queue.pop(0)
			while queue and A[i]>=A[queue[-1]]:
				queue.pop()
			queue.append(i)
		out.append(A[queue[0]])
		return out