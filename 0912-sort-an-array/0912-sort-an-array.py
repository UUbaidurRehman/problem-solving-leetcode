class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        res = []
        heapify(heap)
        for i in nums:
            heappush(heap, i)
        while heap:
            res.append(heappop(heap))
        return res