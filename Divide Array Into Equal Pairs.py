class Solution(object):
    def divideArray(self, nums):
        from collections import Counter
        count = Counter(nums)
        for c in count.values():
            if c % 2 != 0:
                return False
        
        return True