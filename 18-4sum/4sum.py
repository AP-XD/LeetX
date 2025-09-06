class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for j in range(len(nums)):
            if j>0 and  nums[j]==nums[j-1]:
                continue
            for i in range(j+1,len(nums)):
                if i>j+1 and nums[i]==nums[i-1]:
                    continue
                l=i+1
                r=len(nums)-1
                while l<r:
                    tsum = nums[i]+nums[r]+nums[l]+nums[j] - target
                    if tsum>0:
                        r-=1
                    elif tsum<0:
                        l+=1
                    else:
                        res.append([nums[j],nums[i],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
        return res