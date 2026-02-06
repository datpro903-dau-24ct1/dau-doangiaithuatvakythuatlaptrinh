class Solution(object):
    def destCity(self, paths):
        start = set()
        end = set()

        for a, b in paths:
            start.add(a)
            end.add(b)

        for city in end:
            if city not in start:
                return city