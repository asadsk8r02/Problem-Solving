class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #max_sum = float('-inf')

        # if k == len(nums):
        #     return sum(nums)/k

        summ = sum(nums[:k])
        max_sum = summ

        for i in range(k,len(nums)):
            summ = summ - nums[i-k] + nums[i]
            max_sum = max(summ, max_sum)

        return max_sum/k