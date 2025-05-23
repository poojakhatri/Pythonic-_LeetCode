class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n  = len(nums) 
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        if min_index > max_index:
            min_index, max_index = max_index, min_index
        
        left_removal = max_index + 1
        right_removal = n - min_index
        mixed_removal = (min_index + 1) + (n-max_index)
        return min(left_removal, right_removal, mixed_removal)

        