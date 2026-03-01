class Solution(object):
    def moveZeroes(self, nums):
        tso=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[tso],nums[i]=nums[i],nums[tso]
                tso+=1