class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index=-1
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                index=i
                break
        nums[:]= nums[index+1:]+nums[0:index+1]
        print(nums)
        l=0
        h=len(nums)-1
        mid=0
        flag=0
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>target:
                h=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                flag=1
                index=(mid+index+1)%(len(nums))
                break
        if flag==1:
            return index
        return -1        