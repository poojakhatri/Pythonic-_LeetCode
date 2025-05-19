class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}   # Dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            complement =  target - num
            if complement in num_map:
                return [num_map[complement], i] # Return indices of two numbers
            num_map[num] = i   # Store the index of the current number in the Dictionary
        