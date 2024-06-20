#User function Template for python3

class Solution:
    def factorial(self, N):
        result = self.fact(N)
        result = [int(x) for x in str(result)]
        return result
    
    def fact(self, N):
        if N == 1 or N == 0:
            return 1
        return N * self.fact(N-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends