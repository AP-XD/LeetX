class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=1
        h=sum(weights)
        res=h
        while l<=h:
            mid=(l+h)//2
            s=0
            c=0
            flag=1
            for i in weights:
                s+=i
                # print(s)
                if s==mid:
                    c+=1
                    s=0
                elif s>mid:
                    c+=1
                    s=i
                if s>mid:
                    flag=0
                    break
                elif s==mid:
                    c+=1
                    s=0
            
            if s!=0:
                c+=1
            # print(c,mid)
            if c<=days and flag==1:
                res=min(res,mid)
                h=mid-1
            else:
                l=mid+1
        return res
