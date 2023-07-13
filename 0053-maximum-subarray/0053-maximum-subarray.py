class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_c = nums[0]
        max_g = nums[0]
        for i in range(1,len(nums)):
            max_c = max(nums[i],max_c + nums[i])
            max_g = max(max_g, max_c)
    
        return max_g