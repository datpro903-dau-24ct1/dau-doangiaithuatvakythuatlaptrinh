class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        ls=[]
        for i in range(len(nums)):
            if nums[i]==target:
                ls.append(i)
        return ls