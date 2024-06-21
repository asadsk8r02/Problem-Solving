#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        return self.binary(arr, 0, n-1)
                
    def binary(self, arr, low, high):
        if low == high:
            return arr[low]  # Only one element left, return it
        
        mid = (low + high) // 2
        
        if arr[mid] < arr[high]:
            return self.binary(arr, low, mid)  # Minimum is on the left side
        else:
            return self.binary(arr, mid + 1, high)
        
            
                

        #complete the function here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends