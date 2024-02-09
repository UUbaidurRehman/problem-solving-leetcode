class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge  = ''
        len1, len2= len(word1),len(word2)
        index = min(len1, len2)
        if len1 < len2:
            for i in range(len1):
                merge = merge + word1[i] + word2[i]
            # merge = merge + word2[i:]
            for i  in range (index,len2):
                merge  = merge  + word2[i]
        elif len1 > len2:
            for i in range(len2):
                merge = merge + word1[i] + word2[i]
            # merge = merge + word2[i:]
            for i  in range (index, len1):
                merge  = merge  + word1[i]
        else:
            for i in range(len2):
               merge = merge + word1[i] + word2[i]
        return merge


            
        