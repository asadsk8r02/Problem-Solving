class Solution:
    def duplicates(self, arr, n): 
        # result = []
        # for i in range(n):
        #     index = arr[i] % n
        #     arr[index] += n

        # # Step 2: Collect all indices that have a value greater than or equal to 2*n
        # result = []
        # for i in range(n):
        #     if arr[i] // n > 1:
        #         result.append(i)

        # # Step 3: If no duplicates, return [-1]
        # if not result:
        #     return [-1]
        
        # return result

        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        result = []        
        for key, value in count_map.items():
            if value > 1:
                result.append(key)
        
        if result:
            return sorted(result)
        else:
            return [-1]
                
    	# code here
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
