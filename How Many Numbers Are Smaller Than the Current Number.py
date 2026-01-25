class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=[]
        for i in range(len(nums)):
            d=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    d+=1
            a.append(d)
        return a