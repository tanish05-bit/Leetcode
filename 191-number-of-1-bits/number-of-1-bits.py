class Solution(object):
    def hammingWeight(self, n):
        a=0
        for i in range(32):
            if (n>>i) &1:
                a+=1
        return(a)