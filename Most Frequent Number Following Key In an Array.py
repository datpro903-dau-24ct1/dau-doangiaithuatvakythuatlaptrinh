class Solution(object):
    def mostFrequent(self, nums, key):
        freq = {}
        max_count = 0
        result = 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                freq[target] = freq.get(target, 0) + 1

                if freq[target] > max_count:
                    max_count = freq[target]
                    result = target
        return result