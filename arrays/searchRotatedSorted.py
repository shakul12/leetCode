class Solution:
    def isrotated(self, arr, fact):
        start=0
        end=len(arr)-1
        while start<end:
            mid=(start+end)//2
            if arr[mid]>arr[mid+1]:
                return fact+mid
            return max(self.isrotated(arr[:mid+1], fact),self.isrotated(arr[mid+1:], fact+mid+1))
        return -1
    def binary(self, arr, target):
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        #unrotate- at point where i+1 <i
        if len(nums)==1:
            if nums[0]== target:
                return 0
            else:
                return -1
        ind=self.isrotated(nums, 0)
        x= self.binary(nums[:ind+1],target)
        if x==-1:
            y=self.binary(nums[ind+1:],target)
            if y==-1:
                return -1
            else:
                return ind+1+y
        else:
            return x
        #binary search
        