class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        maxi=0
        while i<len(nums) and i<=maxi:
            maxi= max(i+nums[i], maxi)
            i+=1
        if i==len(nums):
            return True
        return False
            
        