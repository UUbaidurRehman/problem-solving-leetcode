class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        set_nums1 = set(nums1)
        for r in range(len(nums2)):
            if nums2[r] in set_nums1 and nums2[r] not in res:
                res.append(nums2[r])
        return res