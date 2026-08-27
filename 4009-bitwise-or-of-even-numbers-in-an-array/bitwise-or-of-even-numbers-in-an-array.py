class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        a=0
        for i in nums:
            if i%2==0:
                a|=i  
        return a  
