class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #length = len(arr)
        # print(length)
        mx= -1
        for i in range(len(arr))[::-1]:
            temp = arr[i]
            arr[i] = mx
            if temp> mx:
                mx = temp
        
        return arr
