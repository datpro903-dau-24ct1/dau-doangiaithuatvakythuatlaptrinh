class Solution(object):
    def sortPeople(self, names, heights):
        p=[]
        for i in range(len(names)):
            p.append((names[i],heights[i]))
        p.sort(key=lambda x: x[1], reverse=True)
        kq=[]
        for name,height in p:
            kq.append(name)
        return kq