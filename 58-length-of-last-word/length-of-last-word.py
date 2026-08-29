class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.strip().split(" ")
        b=len(a)
        return(len(a[b-1]))