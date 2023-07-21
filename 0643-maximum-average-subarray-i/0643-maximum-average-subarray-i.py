class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')

        if k == len(nums):
            return sum(nums)/k

        summ = sum(nums[:k])
        max_avg = summ/k

        for i in range(k,len(nums)):
            summ = summ - nums[i-k] + nums[i]
            avg = summ/k
            max_avg = max(avg, max_avg)

        return max_avg