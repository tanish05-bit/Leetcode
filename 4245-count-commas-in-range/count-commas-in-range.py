class Solution(object):
    def countCommas(self, n):
        a=0
        for i in range(1,n+1):
            if i >= 1000:
                a+=1

        return a