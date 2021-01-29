def helper(str,i,j,dp):
	if j>j:
		return 0

	if dp[i][j] !=-1:
		return dp[i][j]

	if i==j:
		dp[i][j]=1

	elif str[i]==str[j]:
		dp[i][j]= helper(str, i+1,j,dp)+helper(str, i,j-1,dp)+1

	else:
		dp[i][j]= helper(str, i+1,j,dp)+helper(str,i,j-1,dp)- helper(str, i+1,j-1,dp)

	return dp[i][j]


def countPS(str):
	dp= [[-1 for i in range(1000)] for j in range(1000)]
	return helper(str,0,len(str)-1,dp)

