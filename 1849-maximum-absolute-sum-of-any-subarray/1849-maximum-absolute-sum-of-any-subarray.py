class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_c = 0
        min_c = 0
        max_g = 0
        for i in range(0,len(nums)):
            max_c = max((nums[i]),(max_c + nums[i]))
            min_c = min((nums[i]),(min_c + nums[i]))
            max_g = max(max_g,abs(max_c),abs(min_c))

        return max_g