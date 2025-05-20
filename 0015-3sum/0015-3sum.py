class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        target = 0
        result =  set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == target:
                    result.add((nums[l], nums[r], nums[i]))
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        return list(result)