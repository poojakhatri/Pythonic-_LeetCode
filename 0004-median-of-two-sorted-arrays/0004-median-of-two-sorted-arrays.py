import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 +  nums2
        merged_array.sort()
        if len(merged_array) % 2 != 0:
            index = int(len(merged_array)/2)
            median = merged_array[index]
            return median
        else:
            index = int(len(merged_array)/2)
            print(merged_array[index -1] + merged_array[index])
            median = float(merged_array[index -1] + merged_array[index])/2
            return median
        