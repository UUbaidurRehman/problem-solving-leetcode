class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        mx= -1
        for i in range(l)[::-1]:
            temp = arr[i]
            arr[i] = mx
            if temp> mx:
                mx = temp
        
        return arr
