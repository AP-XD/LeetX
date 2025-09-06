class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]:
                nums[j+1]=nums[i+1]
                j+=1
        return j+1