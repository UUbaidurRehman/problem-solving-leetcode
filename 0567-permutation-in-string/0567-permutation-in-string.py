class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        l, r = 0, len(s1)-1
        a = [0]*26
        b = [0]*26
        for i in range(len(s1)):
            a[ord(s1[i]) - ord('a')  ] += 1
            b[ord(s2[i]) - ord('a') ] += 1
        
        # for i in (s2[l:r+1]):
        #         b[ord(i) - ord('a') ] += 1
        while r< len(s2):
            if a == b:
                return True
            # c = sum(1 for j in range(26) if a[j] == b[j])
            # if c == 26:
            #     return True
            b[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r<len(s2):
                b[ord(s2[r]) - ord('a')] += 1
        return a==b