class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_unique = list(set(nums))
        if len(nums) == len(nums_unique):
            return False
        else:
            return True