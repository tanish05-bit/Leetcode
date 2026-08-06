class Solution(object):
    def smallestNumber(self, n, t):
        j=True
        while j is True:
            product=1
            for i in str(n):
                product*=int(i)
            if product%t!=0:
                n+=1
                continue
            else:
                return(n)
                j=False




        