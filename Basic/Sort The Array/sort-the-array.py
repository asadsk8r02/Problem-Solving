#User function Template for python3
class Solution:
    # def sortArr(self, arr, n):
    #     return self.mergesort(arr)
        
    # def mergesort(self, arr):
    #     if len(arr)<=1:
    #         return arr
    #     mid = len(arr)//2
    #     left = self.mergesort(arr[:mid])
    #     right = self.mergesort(arr[mid:])
    #     return self.merge(left,right)
        
    # def merge(self, left, right):
    #     merged = []
    #     m = len(left)
    #     n = len(right)
    #     i = 0
    #     j = 0
    #     while i<m and j<n:
    #         if left[i] <= right[j]:
    #             merged.append(left[i])
    #             i += 1
    #         else:
    #             merged.append(right[j])
    #             j += 1
                
    #     while i<m:
    #         merged.append(left[i])
    #         i += 1
    #     while j<n:
    #         merged.append(right[j])
    #         j += 1
                
    #     return merged
    # def sortArr(self, arr, n):
    #     return self.selectionsort(arr)
    
    # def selectionsort(self, arr):
    #     n = len(arr)
    #     for i in range(n-1):
    #         min_idx = i
    #         for j in range(i+1, n):
    #             if arr[j]<arr[min_idx]:
    #                 min_idx = j
    #         arr[min_idx], arr[i] = arr[i], arr[min_idx]
    #     return arr
    
    def sortArr(self, arr, n):
        arr.sort()
        return arr
            
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.sortArr(arr, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends