class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ones = 0
        twos=0
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        i = 0
        while zeros > 0:
            nums[i] = 0
            zeros -= 1
            i += 1
        while ones > 0:
            nums[i] = 1
            ones -= 1
            i += 1
        while twos > 0:
            nums[i] = 2
            twos -= 1
            i += 1
        return nums