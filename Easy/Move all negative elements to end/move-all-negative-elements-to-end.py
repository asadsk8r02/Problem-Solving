#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        
        # Array append method takes O(N) space as well
        # neg_arr = []
        # pos_arr = []
        # for i in range(n):
        #     if arr[i]>0:
        #         pos_arr.append(arr[i])
        #     elif arr[i]<0:
        #         neg_arr.append(arr[i])

        # arr[:] = pos_arr + neg_arr
        
        # return arr
        
        
        # Stack Method takes O(N) space as well.
        # neg = []
        # pos = []
        
        # for i in range(n):
        #     if arr[i]>0:
        #         pos.append(arr[i])
        #     else:
        #         neg.append(arr[i])
                
        # i = n-1
        
        # while neg:
        #     arr[i] = neg.pop()
        #     i-=1
            
        # while pos:
        #     arr[i] = pos.pop()
        #     i-=1
            
        # 
        
        tmp1 = []  #Initializing an empty list to store positive elements.
        tmp2 = []  #Initializing an empty list to store negative elements.
        
        #Iterating over each element in the array.
        for i in arr:
            if i >= 0:   #If the element is positive, add it to the temporary positive list.
                tmp1.append(i)
            else:        #If the element is negative, add it to the temporary negative list.
                tmp2.append(i)
        
        c = 0   #Initializing a counter variable to keep track of the index in the original array.
        
        #Iterating over the elements in the combined positive and negative lists.
        for i in tmp1 + tmp2:
            arr[c] = i   #Replacing the value in the original array with the value from the temporary lists.
            c += 1 
        
        # Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends