class Solution:
    def check(self, nums: List[int]) -> bool:
        k=-1
        z=0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                z+=1
        
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                k=i
                break
        print(k)
        if k==-1:
            return True
        if z>1:
            return False
        for i in range(k+1,len(nums)):
            if nums[0]<nums[i]:
                print(i)
                return False
        return True