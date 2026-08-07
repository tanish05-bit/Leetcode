class Solution(object):
    def findMissingElements(self, nums):
        L=[]
        for i in range(min(nums),max(nums)):
            if i in nums:
                continue
            else:
                L.append(i)
        return(L)

        