class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "" and needle == "":
            return 0
        if needle =="":
            return 0
        count = haystack.find(needle)
        if count >= 0:
            return count
        else:
            return -1