class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        res = 0
        
        for i in range(n):
            for j in range(n):
                if colors[i] != colors[j]:
                    res = max(res, abs(i - j))
        
        return res