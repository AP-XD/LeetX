class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=-1
        j=0
        k=len(nums)-1
        while i<len(nums):
            i+=1
            if i>k:
                break
            elif nums[j]==0:
                j+=1
            elif nums[k]==2:
                k-=1
                i-=1
            elif nums[i]==0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
                i-=1
            elif nums[i]==2:
                nums[k],nums[i]=nums[i],nums[k]
                k-=1
                i-=1
