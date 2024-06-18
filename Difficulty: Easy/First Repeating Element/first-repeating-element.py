#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        count_map = {}
        first_idx = n-1
        for i in range(n):
            if arr[i] in count_map:
                first_idx = min(first_idx,count_map[arr[i]][0])
                pass
            else:
                count_map[arr[i]] = [i]
          
        if first_idx == n-1:
            return -1
        else:
            return first_idx + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends
