#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        if s == 0:
            for i in range(n):
                if arr[i] == 0:
                    return [i + 1, i + 1]
            return [-1]

        # Initialize pointers and the current sum
        left = 0
        curr_sum = 0

        # Traverse the array with the right pointer
        for right in range(n):
            # Add the current element to the current sum
            curr_sum += arr[right]

            # While current sum is greater than the target sum, subtract elements from the left
            while curr_sum > s and left <= right:
                curr_sum -= arr[left]
                left += 1

            # If the current sum is equal to the target sum, return the indices
            if curr_sum == s:
                return [left + 1, right + 1]  # +1 for 1-based indexing

        # If no subarray is found, return [-1]
        return [-1]
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends