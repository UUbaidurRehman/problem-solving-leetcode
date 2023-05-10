class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        s=0
        for i in range(len(accounts)):
            s=0
            for j in range(len(accounts[i])):
                s += accounts[i][j]
            if m <= s:
                m = s   
        return m