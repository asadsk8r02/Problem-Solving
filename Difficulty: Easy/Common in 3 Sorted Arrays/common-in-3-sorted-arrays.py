#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        new_list = list(set(A)) + list(set(B)) + list(set(C))
        count_map = {}
        result = []
        n = len(new_list)
        for i in range(n):
            if new_list[i] not in count_map:
                count_map[new_list[i]] = 1
            else:
                count_map[new_list[i]] += 1
                
            if count_map[new_list[i]]==3:
                result.append(new_list[i])
                

        return sorted(result)
                
        
        # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends