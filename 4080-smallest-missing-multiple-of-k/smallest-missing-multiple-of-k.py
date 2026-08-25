class Solution(object):
    def missingMultiple(self, nums, k):
        n=1
        m=True
        L=[]
        for i in nums:
            if i%k==0:
                L.append(i)
            else:
                continue
        L.sort()
        while m is True:
            if k*n in L:
                n+=1
            else:
                return(k*n)
                k=False

