class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        # print(length)
        mx= -1
        for i in range(length)[::-1]:
            temp = arr[i]
            arr[i] = mx
            if temp> mx:
                mx = temp
        
        return arr



        # for i in range(length ):
        #     if i==length-1:
        #         arr[i] = -1
        #         return arr
        #     for j in range(i, length-1):                    
        #         if arr[i+1] > arr[j]:
        #             max = arr[j]
        # return arr

