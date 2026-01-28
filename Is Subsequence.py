class Solution(object):
    def isSubsequence(self, s, t):
        a=0
        for c in t:
            if a<len(s) and s[a]==c:
                a+=1
        return a==len(s)