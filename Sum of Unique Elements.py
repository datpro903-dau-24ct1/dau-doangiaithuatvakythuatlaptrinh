class Solution(object):
    def sumOfUnique(self, nums):
        from collections import Counter
        freq = Counter(nums)
        
        total = 0
        for num in freq:
            if freq[num] == 1:
                total += num
        
        return total
        