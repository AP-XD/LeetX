class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        mini=nums[0]
        maxi=nums[len(nums)-1]
        ans=0
        k=[]
        l=[]
        for i in nums:
            mini=min(mini,i)
            k.append(mini)
        for i in range(len(nums)-1,-1,-1):
            maxi=max(maxi,nums[i])
            l.append(maxi)
        l[:]=l[::-1]
        for i in range(len(nums)):
            ans=max(ans,l[i]-k[i])
        return ans