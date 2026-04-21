class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        max_altitude = 0
        for g in gain:
            current += g
            max_altitude = max(max_altitude, current)
        return max_altitude