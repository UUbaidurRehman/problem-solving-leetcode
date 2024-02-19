class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums))[i+1:len(nums):1]:
        #         if nums[i]+nums[j] == target:
        #             return i , j

        dict = {}
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n],i 
            else:
                dict[target-n] = i 
                