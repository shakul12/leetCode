class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            currMax= currMax+nums[i]
            currMax= max(currMax, nums[i])
            maxi=max(currMax, maxi)
        return maxi
        