def myPow( x, n):
        if n ==0:
            return 1
        else:
            return x * myPow(x,n-1)
print(myPow(x=0.00001,n=2147483647))

def myPow(x, n):
        if n == 0:
            return 1
        res = 1
        while n != 0:
            if n > 0:
                res = x*res
                n -= 1
            if  n < 0:
                res = 1/x*res
                n += 1
        return res
print(myPow(0.00001,2147483647))


class Solution(object):
    def myPow(self, x, n):
        return pow(x,n)


class Solution(object):
    def myPow(self, x, n):
        return x**n