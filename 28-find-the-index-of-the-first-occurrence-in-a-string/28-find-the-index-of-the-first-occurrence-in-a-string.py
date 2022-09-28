class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) - len(needle) + 1:
            print(i)
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i + j] == needle[j]:
                    j += 1
                    continue
                print(i, j)
                if j == len(needle):
                    return i
                else:
                    i = i+1
            else:
                i += 1
                
        return -1
                