#User function Template for python3

def getMinMax(a, n):
    minele = a[0]
    maxele = a[0]
    for i in range(1,n):
        if a[i]<minele:
            minele = a[i]
        if a[i]>maxele:
            maxele = a[i]
    return [minele, maxele]
        
        
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends