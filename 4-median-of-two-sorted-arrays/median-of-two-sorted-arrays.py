class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)


        res = nums1 + nums2
        res.sort()
                
        l = len(res)
        li= l / 2
        
        if l % 2 == 0:
            return (res[li] + res[li-1]) / 2.0
        else :
            return float(res[li])

