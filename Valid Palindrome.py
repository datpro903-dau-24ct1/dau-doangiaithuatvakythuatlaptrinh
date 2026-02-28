class Solution(object):
    def isPalindrome(self, s):
        w=""
        for i in s:
            if i.isalnum():
                w+=i.lower()
        return w==w[::-1]