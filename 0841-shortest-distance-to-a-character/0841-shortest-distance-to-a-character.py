class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        arr = []
        for i in range(len(s)):
            if s[i] == c:
                arr.append(i)
        for j in range(len(s)):
            closest = []
            for d in range(len(arr)):
                closest.append(abs(j-arr[d]))
            answer.append(min(closest)) 
        return answer