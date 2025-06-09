class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        pro = {}
        i = 0
        for ele in s:
            pro[indices[i]]= ele
            i += 1
        result = ""
        for i in sorted(pro.keys()):
            result += pro[i]
        return result
                