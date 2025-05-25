class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result