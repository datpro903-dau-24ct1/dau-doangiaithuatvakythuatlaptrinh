class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        box = {}
        for num in range(lowLimit, highLimit + 1):
            s = sum(int(d) for d in str(num))
            box[s] = box.get(s, 0) + 1
        return max(box.values())