class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left=0
        right=len(A)-1
        lmax=0
        rmax=0
        sum=0
        while left<right:
            if A[left]<A[right]:
                lmax=max(lmax, A[left])
                sum+=lmax-A[left]
                left+=1
            else:
                rmax=max(rmax, A[right])
                sum+=rmax-A[right]
                right-=1
        return sum