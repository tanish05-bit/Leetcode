class Solution(object):
    def countCommas(self, n):
        if n<=999:
            return 0
        a=0
        b=1000
        while b <=n:
            a+=n-b+1
            b*=1000
        return(a)       