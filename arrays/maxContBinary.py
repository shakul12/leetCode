class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums=0
        hashmap={}
        max_len=0
        end=-1
        for i in range(len(nums)):
            if nums[i]==0:
                sums-=1
            else:
                sums+=1
            if (sums == 0): 
                max_len = i + 1
                end = i
            if sums in hashmap:
                if max_len<i-hashmap[sums]:
                    max_len=i-hashmap[sums]
                    end=i
            else:
                hashmap[sums]=i
        return max_len
                    