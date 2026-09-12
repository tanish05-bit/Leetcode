class Solution(object):
    def isPalindrome(self, s):
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i.lower())
        return a==a[::-1]