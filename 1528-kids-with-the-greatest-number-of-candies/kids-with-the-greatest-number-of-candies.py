class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new=[x+extraCandies for x in candies]
        return(map(lambda x:x>=max(candies),new))