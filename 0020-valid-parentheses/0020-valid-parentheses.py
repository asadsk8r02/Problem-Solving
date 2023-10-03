class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1 or len(s)%2 != 0:
            return False
        
        stack = []
        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0