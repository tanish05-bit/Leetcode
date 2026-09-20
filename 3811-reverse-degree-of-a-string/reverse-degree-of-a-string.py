class Solution(object):
    def reverseDegree(self, s):
        a=0
        b=1
        for i in s:
            a+=(27-(ord(i)-96))*b
            b+=1
        return(a)