#User function Template for python3

class Solution:
     def reverseWord(self, str: str) -> str:
        #  return s[::-1]
        str = list(str)
        start = 0
        end = len(str)-1
        while start<end:
            str[start], str[end] = str[end], str[start]
            start += 1
            end -= 1
            
        return ''.join(str)
        #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends