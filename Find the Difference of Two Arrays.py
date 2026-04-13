class Solution(object):
    def findDifference(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        
        o1 = list(s1 - s2)
        
        o2 = list(s2 - s1)
        
        return [o1, o2]