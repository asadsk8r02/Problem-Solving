#User function Template for python3

class Solution:
    
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, n):
        sum_c = arr[0]
        sum_g = arr[0]
        
        for i in range(1, n):
            sum_c  = max(arr[i], arr[i] + sum_c)
            sum_g = max(sum_c, sum_g)
            if sum_c < 0:
                sum_c = 0
                
        return sum_g
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends