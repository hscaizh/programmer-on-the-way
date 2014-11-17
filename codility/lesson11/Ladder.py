#author:hscaizh
#create on Nov 6, 2014

'''
题目:
高中常见题,上楼梯,一次可以上一个台阶或者两个台阶,问上到第N层台阶一共有多少种方法

思路:
很容易想到 F[N] = F[N-1]+F[N-2],F[0]=1,F[1]=1 
题目要求O(N),因此动态规划足以达到目标
由于大数处理,题目中要求返回 mod 2^B[i]之后的值,涉及到了一点点模数的性质

复杂度分析:
假定模运算为O(1),算法复杂度显然为O(N)

实现见代码.

解题地址:https://codility.com/demo/results/demoC99T4T-FH7/
'''


def solution(A, B):
    L = len(A)
    if L <= 0:
        return []
        
    F = [0]*(L+1)
    F[0] = 1
    F[1] = 1
    
    m = pow(2,30)
    for i in xrange(2,L+1):
        F[i] = (F[i-1]+F[i-2]) % m
    
    retv = []
    for i in xrange(L):
        retv.append(F[A[i]]%pow(2,B[i]))
    
    return retv


