class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        while low<high:
            mid=(low+high)//2
            if target<nums[mid]:
                high=mid
            elif target>nums[mid]:
                low=mid+1
            else:
                return mid
        if target<nums[mid]:
            return mid
        else:
            return mid+1