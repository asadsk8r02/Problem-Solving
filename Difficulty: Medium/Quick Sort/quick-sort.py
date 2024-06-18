#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # Hoare's
        # if low<=high:
        #     p = self.partition(arr,low,high)
        #     self.quicksort(arr, low, p)
        #     self.quicksort(arr, p+1, high)
        if low<high:
            p = self.partition(arr,low,high)
            self.quickSort(arr, low, p-1)
            self.quickSort(arr, p+1, high)
        # code here
    
    def partition(self,arr,low,high):
        # Hoare's
        # pivot = arr[low]
        # i = low - 1
        # j = high + 1
        
        # while True:
        #     i+=1
        #     while arr[low]<arr[pivot]:
        #         i+=1
                
        #     j-=1
        #     while arr[high]>arr[pivot]:
        #         j-=1
                
        #     if i>=j:
        #         return j
                
        #     arr[i], arr[j] = arr[j], arr[i]
        
        # Lomuto
        pivot=arr[high]
        i = low-1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
        
        
            
            
        # code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends