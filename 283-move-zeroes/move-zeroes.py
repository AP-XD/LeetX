class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                break
        for j in range(i,len(nums)):
            if nums[i]==0:
                if nums[j]==0:
                    continue
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                