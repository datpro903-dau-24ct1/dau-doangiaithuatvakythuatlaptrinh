class Solution(object):
    def findClosestNumber(self, nums):
        c = nums[0]
        
        for x in nums:

            if abs(x) < abs(c):
                c = x

            elif abs(x) == abs(c) and x > c:
                c = x
        
        return c