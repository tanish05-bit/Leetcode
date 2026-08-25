class Solution(object):
    def missingMultiple(self, nums, k):
        i=True
        n=1
        while i is True:
            if k*n in nums:
                n+=1
            else:
                return(k*n)
                i=False


