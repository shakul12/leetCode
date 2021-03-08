class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        merged= []
        for inte in intervals:
            if not merged or merged[-1][1]<inte[0]:
                merged.append(inte)
            else:
                merged[-1][1]= max(merged[-1][1], inte[1])
        return merged