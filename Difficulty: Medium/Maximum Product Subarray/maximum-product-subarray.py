#User function Template for python3
class Solution:
	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
	    pre_product = 1
	    suf_product = 1
	    product = float('-inf')
	    for i in range(n):
	        pre_product *= arr[i]
	        suf_product *= arr[n-i-1]
	        product = max(product, max(pre_product, suf_product))
	        if pre_product == 0:
	            pre_product = 1
	        if suf_product == 0:
	            suf_product = 1
	    return product
	   # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends