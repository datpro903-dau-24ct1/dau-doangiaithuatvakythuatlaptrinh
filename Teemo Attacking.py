class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        t=0
        for i in range(len(timeSeries)-1):
            d=timeSeries[i+1]-timeSeries[i]
            t+= min(d,duration)
        return t+duration      