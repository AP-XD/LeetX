class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=1
        h=len(nums)-1
        if h==0:
            return 0
        if nums[h]>nums[h-1]:
            return h
        if nums[0]>nums[1]:
            return 0
        h=len(nums)-2
        while l<=h:
            mid=(l+h)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                h=mid