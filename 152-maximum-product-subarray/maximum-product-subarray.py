class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax=1
        cmin=1
        ans=max(nums)
        for n in nums:
            if n==0:
                cmax,cmin=1,1
            tmp=cmax
            cmax=max(n,cmax*n,cmin*n)
            cmin=min(n,tmp*n,cmin*n)
            ans=max(ans,cmax)
        return ans