class Solution(object):
    def findFinalValue(self, nums, original):
        a=set(nums)
        while original in a:
            original *=2
        return (original)


        
        