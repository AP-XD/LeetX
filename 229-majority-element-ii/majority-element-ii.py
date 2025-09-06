class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1,el2=-1e9,-1e9
        c1,c2,cnt1,cnt2=0,0,0,0
        for i in nums:
            if c1==0 and i!=el2:
                el1=i
                c1+=1
            elif c2==0 and i!=el1:
                el2=i
                c2+=1
            elif i==el1:
                c1+=1
            elif i==el2:
                c2+=1
            else:
                c1-=1
                c2-=1
            print(el1,el2)
        for i in nums:
            if el1==i:
                cnt1+=1
            if el2==i:
                cnt2+=1
        
        mini=len(nums)//3
        print(el1,el2)
        if cnt1>mini and cnt2>mini and el1!=el2:
            return el1,el2
        elif cnt1>mini:
            return [el1]
        elif cnt2>mini:
            return [el2]
        else:
            return []