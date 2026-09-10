class Solution(object):
    def singleNumber(self, nums):
        setnum=list(set(nums))
        for i in setnum:
            if nums.count(i)==1:
                return(i)