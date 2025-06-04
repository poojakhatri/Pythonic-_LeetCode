class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        last = intervals[0]
        unique = []
        for ele in intervals:
            if ele[0] <= last[1]:
                last[1] = max(last[1], ele[1])
            else:
                unique.append(last)
                last = ele
        unique.append(last)
        return unique
        