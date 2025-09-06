class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        ind=-1
        for i in range(n-2,-1,-1):
            # print(nums[i+1])
            if nums[i+1]>nums[i]:
                ind = i
                break
        # print(ind)
        if ind==-1:
            nums[:]=nums[::-1]
        else:
            for i in range(n-1,ind,-1):
                if(nums[i]>nums[ind]):
                    nums[i],nums[ind]=nums[ind],nums[i]
                    break
            # # print(nums)
            # ans=nums[ind+1:n]
            # ans=ans[::-1]
            # # print(ans)
            nums[ind+1:]=reversed(nums[ind+1:])
        
        
# [3,1,2,3,4,5,5,6]
# [3,1,2,3,4,5,6,5]
# [3,1,2,3,4,6,5,5]
# [3,1,2,3,5,4,5,6]