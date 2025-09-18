import copy
class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        n=len(b)
        if m*k>n:
            return -1
        l=min(b)
        s=0
        c=0
        o=0
        ult=0
        res=max(b)
        # q=list(set(copy.deepcopy(b)))
        
        # q.sort()
        
        h=max(b)
        while l<=h:
            mid=(l+h)//2
            a=mid
            j=copy.deepcopy(b)
            flag=1
            o=0
            for i in range(n):
                if j[i]<=a:
                    j[i]=-1
            c=0
            s=0
            for i in range(n):
                if j[i]==-1 :
                    s+=1
                else:
                    s=0
                if s==k:
                    s=0
                    c+=1
                if c==m:
                    res=min(res,a)
                    # print(res)
                    o=1
                    ult=1
                    break
            if o==1:
                h=mid-1
            else:
                l=mid+1
        if ult==1:
            return res
        return -1

