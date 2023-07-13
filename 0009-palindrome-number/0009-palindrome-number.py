class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            y = str(x)
            z = str(x)[::-1]
            if y==z:
                return True
        