class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for start in range(len(nums)-1):
        #     for end in range(start+1,len(nums)):
        #         if nums[start] == nums[end] and abs(start - end) <= k:
        #             return True

        num_indices = {}  
        
        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True
            num_indices[num] = i

        return False