#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        for i in range(n):
            if arr.count(arr[i]) == 1:
                return arr[i]
        
        return 0
        # Complete the function



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends