class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sums=0
        maps= {0:1}
        for i in range(len(nums)):
            sums+=nums[i]
            if sums-k in maps:
                count+=1
            if sums in maps:    
                maps[sums]+=1
            else:
                maps[sums]=1
        return count
            
        
            
        