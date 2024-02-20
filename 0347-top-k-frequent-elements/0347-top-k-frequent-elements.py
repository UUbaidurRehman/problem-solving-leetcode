class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter ={}
        # for num in nums:
        #     counter[num] = counter.get(num,0) + 1
        # freq_element = sorted(counter.keys() ,key = lambda x : counter[x] , reverse = True)[:k]
        # return freq_element

        dits={}
        for word in nums:
                if word in dits.keys():
                    dits[word] += 1
                else:
                    dits[word] = 1
        sorted_d = collections.OrderedDict(sorted(dits.items(), key=lambda item: item[1],  reverse=True)[:k])
        return sorted_d.keys()