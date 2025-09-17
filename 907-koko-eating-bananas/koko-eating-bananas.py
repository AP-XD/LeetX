import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        high=max(piles)
        ans=high
        while l<=high:
            mid=(l+high)//2
            s=0
            
            for i in piles:
                s+=math.ceil(i/mid)
            if s<=h:
                ans=min(ans,mid)
                high=mid-1
            else:
                l=mid+1
        return ans
