class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s, d):
            if len(s) == 0:
                return set()
            elif len(s) == 1:
                if s in d:
                    return s
                return set()
            
            res = set()
            for i in range(len(s)):
                curr_word = s[:i+1]
                if curr_word in d:
                    if i == len(s) - 1:
                        res.add(curr_word)
                    else:
                        other_words = helper(s[i+1:], d)
                        for w in other_words:
                            res.add(curr_word + " " + w)
                            
            return list(res)
        return helper(s, wordDict)
                    