class Solution(object):
    def canAliceWin(self, n):
        a=10
        t=0
        while n>=a:
            n-=a
            a-=1
            t=1-t
        return t!=0