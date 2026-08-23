class Solution(object):
    def checkDivisibility(self, n):
        n=str(n)
        sums=0
        product=1
        for i in n:
            sums+=int(i)
            product*=int(i)
        if int(n)%(sums+product)==0:
            return True
        else:
            return False


