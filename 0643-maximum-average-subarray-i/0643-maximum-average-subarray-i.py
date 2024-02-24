class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr = []
        summ = sum(nums[0:k])
        for i in range(len(nums)-k+1):
            average = summ/k
            arr.append(average)
            if i < len(nums)-k:
                summ = summ - nums[i] + nums[i+k]
        return (max(arr))
        

        