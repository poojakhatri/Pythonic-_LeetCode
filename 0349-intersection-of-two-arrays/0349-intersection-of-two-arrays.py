class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for ele in nums1:
            if ele in nums2 and ele not in result:
                result.append(ele)
        return result


        