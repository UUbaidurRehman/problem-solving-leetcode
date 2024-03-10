class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_ = {}

        for i in range(len(nums1)):
            map_[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in map_:
                map_[nums2[i]] = 2

        res = []
        keys = map_.keys()
        for key in keys:
            if map_[key] == 2:
                res.append(key)
        return res
