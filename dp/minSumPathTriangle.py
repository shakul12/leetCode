class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    def minimumTotal(self, A):
        dp=A
        for i in range(1,len(A)):
            dp[i][0]+= dp[i-1][0]
            for j in range(1,i):
                dp[i][j]+=min(dp[i-1][j-1], dp[i-1][j])
            dp[i][i]+=dp[i-1][i-1]
        
        ans=999999
        for i in range(len(A)):
            ans=min(ans,dp[len(A)-1][i])
        return ans
