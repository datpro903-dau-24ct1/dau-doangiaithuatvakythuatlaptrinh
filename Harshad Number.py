class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        total = 0
        temp = x
        
        while temp > 0:
            total += temp % 10
            temp //= 10
        if x % total == 0:
            return total
        
        return -1