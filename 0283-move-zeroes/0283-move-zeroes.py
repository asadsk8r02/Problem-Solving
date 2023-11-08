class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = []
        for i in range(len(nums)):
            if nums[i]==0:
                x.append(i)

        for idx in reversed(x):
            nums.pop(idx)
            nums.append(0)

        # left = 0
        # for right in range(len(nums)):
        #     if nums[right] != 0:
        #         nums[right], nums[left] = nums[left], nums[right]
        #         left += 1


        
        