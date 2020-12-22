def numTrees(A):
	dp= {0:1,1:1}
	for i in range(2,A+1):
		dp[i]=0
		for j in range(1, i):
			dp[i]=dp[i]+dp[i-j-1]*dp[j] ##catalan number
	return dp[A]
