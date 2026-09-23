class Solution(object):
    def findFinalValue(self, nums, original):
        while original in set(nums):
            original *=2
        return (original)


        
        