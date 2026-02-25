class Solution(object):
    def passThePillow(self, n, time):
        t = time % (2*(n-1))
        if t < n:
            return t+1
        else:
            return 2*(n-1)-t+1