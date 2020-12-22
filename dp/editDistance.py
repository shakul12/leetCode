def editDistance(A,B):
	dp= [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
	for i in range(len(A)+1):
		dp[i][0]=i
	for j in range(len(B)+1):
		dp[0][j]=j
	for i in range(len(A)):
		for j in range(len(B)):
			rep= dp[i][j]+ (0 if A[i]==B[j] else 1)
			ins= dp[i+1][j]+1
			dro= dp[i][j+1]+1
			dp[i+1][j+1]= min(rep, ins, dro)
	return dp[len(A)][len(B)]