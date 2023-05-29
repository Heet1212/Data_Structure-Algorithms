"""
Problem Description
Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

1 <= A[i] <= 109



Input Format
The first argument is an integer array A.

The second argument is integer B.



Output Format
Return the Bth smallest element in given array.
"""
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
        A=list(A)
        for i in range(0,B):
            min_id =i

            for k in range(i+1,len(A)):
                if A[min_id]>A[k]:
                    min_id=k

            
            A[min_id],A[i]=A[i],A[min_id]    
            
        return A[B-1]      
