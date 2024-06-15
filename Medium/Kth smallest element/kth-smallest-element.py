#User function Template for python3

# class Solution:
#     def kthSmallest(self,arr, l, r, k):
#         self.quicksort(arr,l,r)
#         return arr[k-1]
#         '''
#         arr : given array
#         l : starting index of the array i.e 0
#         r : ending index of the array i.e size-1
#         k : find kth smallest element and return using this function
#         '''
#     def partition(self,arr,l,r):
#         pivot = arr[l]
#         i = l-1
#         j = r+1
        
#         while True:
#             i += 1
#             while arr[i] < pivot:
#                 i += 1
                
#             j -= 1
#             while arr[j] > pivot:
#                 j -= 1
                
#             if i>=j:
#                 return j
                
#             arr[i], arr[j] = arr[j], arr[i]
            
#     def quicksort(self, arr, l, r):
#         if l<r:
#             p = self.partition(arr,l,r)
#             self.quicksort(arr,l,p)
#             self.quicksort(arr,p+1,r)

# class Solution:
#     def kthSmallest(self,arr, l, r, k):   
#         arr.sort()
#         return arr[k-1]

class Solution:
    # def kthSmallest(self, arr, l, r, k):
    #     return self.binarysearch(arr, 1, 10000, l, r, k)
        
    # def binarysearch(self, arr, low, high, l, r, k):
    #     count = 0
    #     possAns = -1
    #     mid = (low + high) // 2
    #     for i in range(l, r + 1):  # inclusive range
    #         if arr[i] <= mid:  # consider elements less than or equal to mid
    #             count += 1
    #             if possAns == -1 or arr[i] > possAns:
    #                 possAns = arr[i]
        
    #     if count == k:
    #         return possAns
    #     elif count < k:
    #         return self.binarysearch(arr, mid + 1, high, l, r, k)
    #     else:
    #         return self.binarysearch(arr, low, mid - 1, l, r, k)
    
    def kthSmallest(self, arr, l, r, k):
        min_val = min(arr[l:r+1])
        max_val = max(arr[l:r+1])
        return self.binarysearch(arr, min_val, max_val, l, r, k)
        
    def binarysearch(self, arr, low, high, l, r, k):
        while low <= high:
            mid = (low + high) // 2
            count = 0
            possAns = -1
            for i in range(l, r + 1):
                if arr[i] <= mid:
                    count += 1
                    if possAns == -1 or arr[i] > possAns:
                        possAns = arr[i]

            if count == k:
                return possAns
            elif count < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
