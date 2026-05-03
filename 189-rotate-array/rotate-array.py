class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p=(n-k)%n
        nums[:]= nums[p:]+nums[0:p] 