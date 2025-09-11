class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)
        flag=0
        llimit,ulimit=(low+high)//2,(low+high)//2
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
            llimit=(low+high)//2
            if target<nums[llimit]:
                high=llimit
            elif target>nums[llimit]:
                low=llimit+1
            else:
                high=llimit
        print(llimit)
        low=0
        high=len(nums)
        while low<high:
            ulimit=(low+high)//2
            if target<nums[ulimit]:
                high=ulimit
            elif target>nums[ulimit]:
                low=ulimit+1
            else:
                low=ulimit+1
        if nums[llimit]==target:
            if nums[ulimit]==target:
                return llimit,ulimit
            else:
                return llimit,ulimit-1
        else:
            if nums[ulimit]==target:
                return llimit+1,ulimit
            else:
                return llimit+1,ulimit-1