class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        k=n*(n+1)//2
        m=sum(nums)
        return abs(k-m)