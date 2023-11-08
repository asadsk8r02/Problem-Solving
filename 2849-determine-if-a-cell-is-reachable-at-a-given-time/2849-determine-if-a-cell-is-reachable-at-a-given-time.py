import math
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t==1 and sx == fx and sy == fy:
            return False
        dist = max(abs(fx-sx),abs(fy-sy))
        if dist<=t:
            return True
        else:
            return False