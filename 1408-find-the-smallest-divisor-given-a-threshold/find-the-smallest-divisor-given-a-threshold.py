import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        h=max(nums)
        res=max(nums)
        while l<=h:
            mid=(l+h)//2
            s=0
            for i in nums:
                s+=math.ceil(i/mid)
            # print(s,mid)
            if s<=threshold:
                res=min(res,mid)
                h=mid-1
                
            else:
                
                l=mid+1
        return res