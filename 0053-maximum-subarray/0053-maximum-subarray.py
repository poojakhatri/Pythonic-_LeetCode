class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        max_= nums[0]

        for ele in nums:
            if total < 0:
                total = 0
            total += ele
            max_ = max(max_, total)
        return max_