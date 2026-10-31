class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        a={"type":0,"color":1,"name":2}
        b=a[ruleKey]
        c=0
        for i in items:
            if i[b]==ruleValue:
                c+=1
        return c