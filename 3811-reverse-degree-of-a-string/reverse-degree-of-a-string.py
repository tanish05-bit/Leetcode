class Solution(object):
    def reverseDegree(self, s):
        a=0
        b=1
        for i in range(len(s)):
            a+=(123-ord(s[i]))*(i+1)
        return (a)