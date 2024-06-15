#User function Template for python3

class Solution:
    def sort012(self,arr,n):
    #     self.quicksort(arr, 0, n-1)
    #     return arr
        
    # def partition(self, arr, low, high):
    #     pivot = arr[low]
    #     i = low - 1
    #     j = high + 1
    #     while True:
    #         i += 1
    #         while arr[i] < pivot:
    #             i += 1
                
    #         j -= 1
    #         while arr[j] > pivot:
    #             j -= 1
                
    #         if i>=j:
    #             return j
                
    #         arr[i], arr[j] = arr[j], arr[i]
            
    # def quicksort(self, arr, low, high):
    #     if low<high:
    #         p = self.partition(arr, low, high)
    #         self.quicksort(arr, low, p)
    #         self.quicksort(arr, p+1, high)
    
        low = 0
        mid = 0
        high = n-1
        
        while mid<=high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid+=1
                low+=1
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high-=1
        return arr
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends