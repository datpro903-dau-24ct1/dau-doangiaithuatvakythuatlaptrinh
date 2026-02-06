class Solution(object):
    def sortPeople(self, names, heights):
        p=[]
        for i in range(len(names)):
            p.append((names[i],heights[i]))
        p.sort(key=lambda x: x[1], reverse=True)
        kq=[]
        for p1 in p:
            kq.append(p1[0])
        return kq