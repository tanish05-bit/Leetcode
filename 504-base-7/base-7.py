class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return("0")
        sign="-" if num<0 else ""
        result=""
        num=abs(num)
        while num>0:
            remainder=num%7
            result+=str(remainder)
            num//=7
        return(sign + result[::-1])
        