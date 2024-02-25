class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        summ = sum(arr[0:k])

        for i in range (len(arr)-k + 1):
            avg = summ/k
            if avg >= threshold:
                counter += 1
            if i+k <len(arr):
                summ  = summ - arr[i] + arr[i+k]
        return counter