class Solution(object):
    def areOccurrencesEqual(self, s):
        from collections import Counter
        
        freq = Counter(s)
        values = list(freq.values())
        
        return len(set(values)) == 1