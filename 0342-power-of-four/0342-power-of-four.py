class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n==1:
        #     return True
        # elif n<=0 or n%4 != 0:
        #     return False
        # else:
        #     return self.isPowerOfFour(n//4)

        #-------------------------------------
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n //= 4
        
        return n == 1

        #------------------------------------
        #return n>0 and log(n,4).is_integer()
        #-----------------------------------
        #return n > 0 and not n & (n - 1)  and len(bin(n)) % 2 


               