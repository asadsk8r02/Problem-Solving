#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        count_map = {0:1}
        sm = 0
        count = 0
        for i in arr:
            if i == 0:
                sm += -1
            else:
                sm += 1
            
            if sm in count_map:
                count += count_map[sm]
                count_map[sm] += 1
            else:
                count_map[sm] = 1
        return count
        #Your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends