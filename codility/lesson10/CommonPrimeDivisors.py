# you can use print for debugging purposes, e.g.
# print "this is a debug message"

'''
题目:
求a,b的所有素数因子是否相同,求Z次
复杂度要求:O(Z*log(max(A)+max(B))^2);

思路:
思路本身挺简单的,求出a,b的最大公约数d,然后a|b一直除a|b和d的最大公约数,如何素数因子相同,
最后的结果肯定是1.

复杂度分析:
while a!=1 段时间 小于 log(a)
while b!=1 段时间 小于 log(b)
单个时间 小于 log(a+b)+log(a)+log(b) ~= O(log(a+b))
最终的时间复杂度为O(Z*log(a+b))

问题:
题目中的时间复杂度没太看懂,O(Z*log((max(A)+max(B))^2))还是O(Z*(logmax(A)+max(B))^2)?

实现见代码.

解题地址:https://codility.com/demo/results/demo9HKX4C-ZAE/
'''

def solution(A, B):
    def gcd(a, b):
        if (a%b == 0):
            return b
        else:
            return gcd(b, a%b)

    def has_same_divisors(a, b):
        d = gcd(a, b)
        a //= d
        b //= d
        while a != 1:
            tmp = a
            a = a//gcd(a,d)
            if a == tmp:
                return False
        while b != 1:
            tmp = b
            b = b//gcd(b,d)
            if b == tmp:
                return False
        return True
    
    N = len(A)
    retv = 0
    for i in xrange(N):
        a, b = A[i], B[i]
        if has_same_divisors(a, b):
            retv += 1
    
    return retv
            
