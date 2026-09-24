class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            a=0
            if nums[i]>9:
                for j in str(nums[i]):
                    a+=int(j)
                if a==i:
                    return(a)
            elif nums[i]==i:
                return(i)
        return(-1)
            
        
        


