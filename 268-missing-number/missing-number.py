class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        sums=n*(n+1)//2
        return(sums-sum(nums))