class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        result = nums[0]
        for ele in nums:
            if total < 0:
                total = 0
            total+=ele
            result = max(total, result)
        return result