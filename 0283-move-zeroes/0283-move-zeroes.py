class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for ele in nums:
            if ele  == 0:
                nums.remove(ele)
                nums.append(ele)

        return nums

        