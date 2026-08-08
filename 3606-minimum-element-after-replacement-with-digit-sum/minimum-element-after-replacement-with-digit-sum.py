class Solution(object):
    def minElement(self, nums):
        L=[]
        a=0
        for i in nums:
            for j in str(i):
                a+=int(j)
            L.append(a)
            a=0
        return min(L)
        