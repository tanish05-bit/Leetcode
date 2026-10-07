class Solution(object):
    def climbStairs(self, n):
        current,previous=1,1
        for i in range(1,n):
            current,previous=current+previous,current
        return(current)
