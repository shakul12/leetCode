class Solution:
    # @param A : string
    # @return an integer
    def check(self,A,k,i):
        A=A[k:i+1]
        if A==A[::-1]:
            return True
        else:
            return False
    def find(self,A, n,dp):
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        if self.check(A,0,n):
            return 0
        ans=99999
        for j in range(n,-1,-1):
            if self.check(A,j,n):
                ans= min(ans, self.find(A,j-1,dp))
        if ans!=99999:
            ans+=1
        dp[n]=ans
        return ans
            
    def minCut(self, A):
        dp={}
        for i in range(len(A)+1):
            dp[i]= -1
        return self.find(A, len(A)-1,dp)
        
