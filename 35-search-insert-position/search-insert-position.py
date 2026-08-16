class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            nums.append(target)
            nums.sort()
            return(nums.index(target))
        else:
            for i in nums:
                if i==target:
                    return(nums.index(i))
                else:
                    continue

