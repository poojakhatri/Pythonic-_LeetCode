class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[:i+1])
            result += c
            s = s[s.index(c):].replace(c, '')
        return result
        