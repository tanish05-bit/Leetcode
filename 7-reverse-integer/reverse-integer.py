class Solution(object):
    def reverse(self, x):
        x=str(x)
        if x[0]=='-':
            x="-"+x[1:][::-1]
        else:
            x=x[::-1]
        if int(x)>2**31-1 or int(x)<-(2**31):
            return (0)
        else:
            return (int(x))

