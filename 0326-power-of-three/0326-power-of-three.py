class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n<=0 or n%3 != 0:
            return False     
        else:
            return self.isPowerOfThree(n//3)

        # if n <= 0:
        #     return False
        
        # max_power_of_three = 3 ** 19  
        
        # return max_power_of_three % n == 0

