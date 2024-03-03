class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_word = {}
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        for i in range(len (pattern)):
            if pattern[i] in dict_word:
                if dict_word[pattern[i]] != s_list[i]: 
                    return False
            else:
                if s_list[i] in dict_word.values():
                    return False
                dict_word[pattern[i]] = s_list[i]
        return True