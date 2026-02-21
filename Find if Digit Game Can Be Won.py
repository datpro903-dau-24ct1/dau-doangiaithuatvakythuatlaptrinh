class Solution(object):
    def canAliceWin(self, nums):
        sum1 = 0
        sum2 = 0

        for n in nums:
            if n < 10:
                sum1 += n
            elif n < 100:
                sum2 += n

        total = sum(nums)

        if sum1 > total - sum1:
            return True

        if sum2 > total - sum2:
            return True

        return False