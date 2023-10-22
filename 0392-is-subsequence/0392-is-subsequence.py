class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        
        for p2 in range(len(t)):
            if p1 < len(s) and t[p2] == s[p1] :
                p1 +=1
        return  p1 == len(s)







        # for i in range(len(s)):
        #     if s[i] in t:
        #         arr.append(t.index(s[i]))
        #         if i != 0:
        #             if arr[i] < arr[i-1]:
        #                 return False
        #     else:
        #         return False
        # return True
