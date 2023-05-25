class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        l=1
        r=A
        ans=-1

        if A==0 or A==1:
            return A
        while l<=r:
            mid=(l+r)//2
            if mid*mid >A:
                r=mid-1
            else:
                ans=max(ans,mid) 
                l=mid+1   

        if (ans*ans==A):
            return ans
        else:
            return -1
