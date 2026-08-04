class Solution(object):
    def maximizeSum(self, nums, k):
        a=max(nums)
        i=0
        total=0 
        while i<k:
            total+= a   
            a+=1          
            i+=1
        return(total)



        