class Solution(object):
    def matrixSum(self, nums):
        a=0
        for i in nums:
            i.sort()
        for i in zip(*nums):
            a+=int(max(i))
        return(a)
            