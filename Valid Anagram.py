class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!= len(t):
            return False
        ss=sorted(s)
        st=sorted(t)
        if ss==st:
            return True
        else:
            return False