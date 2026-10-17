class Solution(object):
    def createTargetArray(self, nums, index):
        L=[]
        for a,b in zip(index,nums):
            L.insert(a,b)
        return L
