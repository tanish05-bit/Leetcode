class Solution(object):
    def sumDivisibleByK(self, nums, k):
        a=set(nums)
        count=0
        for i in a:
            b=nums.count(i)
            if b%k==0:
                count+=i*b
            else:
                continue
        return(count)



        