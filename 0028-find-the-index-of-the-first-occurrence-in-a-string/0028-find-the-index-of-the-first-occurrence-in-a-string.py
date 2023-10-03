class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
        # new = haystack.replace(needle,'A')
        # if (new == haystack): return -1
        # else: return new.index('A')

        # if needle == haystack:
        #     return 0
        # i = 0
        # j = len(needle)
        # while j <= len(haystack):
        #     currentNeedle = haystack[i:j]
        #     if currentNeedle == needle:
        #         return i
        #     i += 1
        #     j += 1
        # return -1

        # if not needle:
        #     return 0
        # if needle not in haystack:
        #     return -1
        # return haystack.index(needle)

        def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0

        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i

        return -1


