class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for k in nums:
            if k!=val:
                nums[i]=k
                i+=1
        return(i)


        