#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        count_map = {}
        count = 0
        for i in range(n):
            difference = k - arr[i]
            if difference in count_map:
                count += count_map[difference]
            
            if arr[i] in count_map:
                count_map[arr[i]] += 1
            else:
                count_map[arr[i]] = 1
        
        return count
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends