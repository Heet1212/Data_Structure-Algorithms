"""Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.

Problem Constraints
-1010 <= A[i], B[i] <= 1010


Input Format
First Argument is a 1-D array representing  A.
Second Argument is also a 1-D array representing B."""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of iBntegers
    def solve(self, A, B):

        n =0 
        m = 0
        
        D=len(A)+len(B)
        c=[0]*D
        list=[]
        for k in range(D):
            if n ==len(A):
                c[k]=B[m]
                m+=1
            elif m==len(B) or A[n] <=B[m]:
                c[k]=A[n]
                n+=1
            else:
                c[k]=B[m]
                m+=1
        return c        

