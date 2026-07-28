class Solution(object):
    def isPalindrome(self, x):
        L=list(str(x))
        reverse=L[::-1]
        return L==reverse
        



        