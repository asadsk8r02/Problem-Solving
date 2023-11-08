class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        x = []
        for i in nums1:
            if i in nums2:
                x.append(i)

        return x

        # return set(nums1).intersection(nums2)