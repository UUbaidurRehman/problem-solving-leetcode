class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1 
        a = [0]*150
        for i in map(ord, s1):
            a[i] +=1
        
        while r < len(s2):
            b= [0]*150 
            for j in map(ord,s2[l:r+1]):
                b[j] +=1
            c = sum(1 for i in range(150) if a[i] == b[i])
            if c == 150:
                return True
            l += 1
            r += 1
        return False 