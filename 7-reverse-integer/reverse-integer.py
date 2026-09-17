class Solution(object):
    def reverse(self, x):
        a=(2**31)-1
        b=-2**31 
        d=0
        if x<0:
            c=-1
        else:
            c=1
        x=abs(x)
        while x!= 0:
            e= x%10
            d=d*10+e
            x//= 10
        d*=c
        if d>a or d<b:
            return 0
        return d