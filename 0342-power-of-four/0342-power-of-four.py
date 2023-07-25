class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        elif n<=0 or n%4 != 0:
            return False
        else:
            return self.isPowerOfFour(n/4)

        # if n<=0:
        #     return False

        # max_power = 4**15
        
        # return max_power % n == 0

               