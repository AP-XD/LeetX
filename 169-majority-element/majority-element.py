class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        st=[]
        top=-1
        for i in range(len(nums)):
            if len(st)==0:
                st.append(nums[i])
                top+=1
            elif nums[i]!=st[top]:
                st.pop()
                top-=1
            else:
                st.append(nums[i])
                top+=1
        return st[top]

