class Solution(object):
    def countEven(self, num):
        s = sum(int(d) for d in str(num))  
        if s % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2