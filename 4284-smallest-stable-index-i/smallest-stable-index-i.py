class Solution(object):
    def firstStableIndex(self, nums, k):
        if len(nums)==1:
            return(0)
        for i in range(len(nums)):
            a=max(nums[0:i+1])-min(nums[i:len(nums)])
            if a<=k:
                return(i)
            elif a>k:
                continue
        return(-1)