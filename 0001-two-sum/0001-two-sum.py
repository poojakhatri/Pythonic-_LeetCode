class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, ele in enumerate(nums):
            complement = target - ele
            if complement in seen:
                return [seen[complement], i]
            seen[ele] = i
