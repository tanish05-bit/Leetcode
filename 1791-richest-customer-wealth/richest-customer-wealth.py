class Solution(object):
    def maximumWealth(self, accounts):
        a=0
        for i in accounts:
            a=max(a, sum(i))
        return a
        
        