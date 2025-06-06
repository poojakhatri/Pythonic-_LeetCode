class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = curr_min = result = nums[0]
        for ele in nums[1:]:
            tmp = curr_max
            curr_max = max(ele, ele*curr_max, ele*curr_min)
            curr_min = min(ele, ele*tmp, ele*curr_min)
            result = max(result, curr_max)
        return result