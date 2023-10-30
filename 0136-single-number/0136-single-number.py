class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = dict()
        for n in nums:
            if n in dic.keys():
                dic[n] = dic[n] + 1
            else:
                dic [n] = 1
        for key in dic.keys():
            if dic[key] == 1:
                return key