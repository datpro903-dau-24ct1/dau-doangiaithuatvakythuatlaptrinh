class Solution(object):
    def checkIfExist(self, arr):
        s=set()
        for nums in arr:
            if 2*nums in s or (nums%2==0 and nums//2 in s) :
                return True
            s.add(nums)
        return False