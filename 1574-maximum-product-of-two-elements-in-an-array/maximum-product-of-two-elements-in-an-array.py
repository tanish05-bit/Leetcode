class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1],nums[j]
        return ((nums[-1]-1)*(nums[-2]-1))