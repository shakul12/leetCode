class graphi:
	def __init__(self,row,col,g):
		self.row=row
		self.col=col
		self.graph=g

	def safe(self,i,j,visited):
		return (i>=0 and j>=0 and i<self.row and j<self.col and not visited[i][j] and self.graph[i][j])
	
	def dfs(self,i,j, visited):
		
		row_call= [-1,-1,-1,0,0,1,1,1]
		col_call= [-1,0,1,-1,1,-1,0,1]
		visited[i][j]=True
		for x in range(8):
			if self.safe(i+row_call[x],j+col_call[x],visited):
				self.dfs(i+row_call[x],j+col_call[x],visited)

	def count(self):
		visited= [[False for x in range(self.col)] for y in range(self.row)]
		count=0
		for i in range(self.row):
			for j in range(self.col):
				if visited[i][j]==False and self.graph[i][j]==1:
					self.dfs(i,j,visited)
					count+=1
		return count


grid = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]


g=graphi(len(grid), len(grid[0]), grid)

print(g.count())
