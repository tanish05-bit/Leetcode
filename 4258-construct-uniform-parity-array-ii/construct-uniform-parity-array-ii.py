class Solution(object):
    def uniformArray(self, nums1):
        a=min(nums1)
        if a%2==1:
            return(True)
        for i in nums1:
            if i%2==1:
                return(False)
        return(True)

        