class Solution(object):
    def capitalizeTitle(self, title):
        a=[]
        for i in title.split():
            if len(i)<3:
                a.append(i.lower())
            else:
                a.append(i.capitalize())
        return " ".join(a)