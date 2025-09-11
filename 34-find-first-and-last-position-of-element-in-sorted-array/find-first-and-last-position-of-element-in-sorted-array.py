class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)
        flag=0
        llimit,ulimit=-1,-1
        while low<high:
            mid=(low+high)//2
            if target<nums[mid]:
                high=mid
            elif target>nums[mid]:
                low=mid+1
            else:
                flag=1
                break
        if flag==0:
            return [-1,-1]
        low=0
        high=len(nums)
        while low<high:
            mid=(low+high)//2
            if target<nums[mid]:
                high=mid
            elif target>nums[mid]:
                low=mid+1
            else:
                llimit=mid
                high=mid
        print(mid)
        low=0
        high=len(nums)
        while low<high:
            mid=(low+high)//2
            if target<nums[mid]:
                high=mid
            elif target>nums[mid]:
                low=mid+1
            else:
                ulimit=mid
                low=mid+1
        return llimit,ulimit