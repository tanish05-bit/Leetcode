class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        a=len(nums)
        for i in range(1,a):
            if nums[i]==nums[i-1]:
                return True
        return False
