class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st=set(nums)
        ans=0

        for i in st:
            if i-1 not in st:
                c=1
                j=i
                while j+1 in st:
                    c+=1
                    j+=1
                ans=max(ans,c)
        return ans