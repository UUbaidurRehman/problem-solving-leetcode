class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        freq = [[] for i in range(len(nums)+1)]

        for n,c in counter.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0 ,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k :
                    return res