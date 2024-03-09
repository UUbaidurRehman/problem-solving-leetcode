class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        N = set(nums1)
        for i in nums2:
            if i in N:
                return i
        return -1